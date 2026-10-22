#!/usr/bin/env python3
"""Dohledání fotek nových zastávek (bez AI a bez API klíčů). Pro každou zastávku ze state.json, která nemá
vestavěnou fotku, najde článek o místě na Wikipedii (ověřený podle vzdálenosti od bodu na mapě), vezme jeho hlavní
fotku z Wikidat nebo z článku (jen volné licence z Wikimedia Commons),
stáhne zmenšenou verzi do photos/places/auto/ a zapíše autora a licenci do photos/places/auto.json.
Používá jen standardní knihovnu Pythonu."""
import json, math, os, re, time, unicodedata, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone, timedelta

UA = {"User-Agent": "cesta-fotky/1.0 (osobni cestovni stranka; https://github.com/enjoythispower-boop/Central-and-South-America)"}
INDEX = "photos/places/auto.json"
DIR = "photos/places/auto"
WIDTH = 1400
RETRY_DAYS = 7     # po kolika dnech zkusit znovu místo, ke kterému se fotka nenašla
MAX_KM = 60        # ostatní články musí ležet nejdál takhle daleko od bodu na mapě
NAME_KM = 300      # článek se stejným názvem jako místo může být dál
# zastávky s ručně vybranou fotkou (stejné klíče jako PHOTO_BY_STOP v index.html)
BUILTIN = {"cancun", "tulum", "ciudad de mexico", "mexico city", "antigua", "san jose", "bogota", "quito", "cusco",
           "la paz", "santiago", "buenos aires"}
COUNTRY_EN = {"Mexiko": "Mexico", "Guatemala": "Guatemala", "Belize": "Belize", "Salvador": "El Salvador",
              "Honduras": "Honduras", "Nikaragua": "Nicaragua", "Kostarika": "Costa Rica", "Panama": "Panama",
              "Kolumbie": "Colombia", "Ekvádor": "Ecuador", "Peru": "Peru", "Bolívie": "Bolivia", "Chile": "Chile",
              "Argentina": "Argentina", "Paraguay": "Paraguay", "Uruguay": "Uruguay", "Brazílie": "Brazil"}

BAD_IMG = re.compile(r"\.svg$|\bmaps?\b|mapa|locator|location|flag|bandera|coat.of.arms|escudo|seal|logo|montage|montaje|collage|panel|skyline.composite", re.I)

def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower()) if unicodedata.category(c) != "Mn").strip()

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-") or "misto"

def get(url, timeout=60):
    for wait in (0, 30, 90):  # při přetížení (429/5xx) chvíli počkat a zkusit znovu
        time.sleep(wait or 1)  # šetrně k Wikimedii
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 and e.code < 500:
                raise
            err = e
    raise err

def api(host, **params):
    params.update(format="json", formatversion=2)
    params.setdefault("action", "query")
    return json.loads(get(f"https://{host}/w/api.php?" + urllib.parse.urlencode(params)))

def km(a, b):
    t = math.radians
    dl, dn = t(b[0] - a[0]), t(b[1] - a[1])
    q = math.sin(dl / 2) ** 2 + math.cos(t(a[0])) * math.cos(t(b[0])) * math.sin(dn / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(q))

def near(pages, stop):
    """Články, které leží u bodu na mapě; rozcestníky a články bez souřadnic vynechá. Článek nazvaný stejně jako
    místo má přednost a stačí mu být do NAME_KM (bod na mapě bývá zadaný jen přibližně), ostatní do MAX_KM."""
    name, out = norm(stop["n"]), []
    for p in pages or []:
        co = (p.get("coordinates") or [None])[0]
        if p.get("missing") or not co or "disambiguation" in (p.get("pageprops") or {}):
            continue
        d = km((stop["lat"], stop["lon"]), (co["lat"], co["lon"]))
        same = norm(p.get("title")).startswith(name)
        if d <= (NAME_KM if same else MAX_KM):
            out.append((not same, d, p))
    return [x[2] for x in sorted(out, key=lambda x: x[:2])]

def image_of(page):
    """Hlavní fotka místa: nejdřív z Wikidat (P18), jinak úvodní obrázek článku; mapy, vlajky a koláže ne."""
    qid = (page.get("pageprops") or {}).get("wikibase_item")
    if qid:
        try:
            r = api("www.wikidata.org", action="wbgetclaims", entity=qid, property="P18")
            for c in r.get("claims", {}).get("P18", []):
                f = c.get("mainsnak", {}).get("datavalue", {}).get("value")
                if f and not BAD_IMG.search(f):
                    return f
        except Exception as e:
            print(f"  wikidata {qid}: {e}")
    f = page.get("pageimage")
    return f if f and not BAD_IMG.search(f) else None

PROPS = dict(prop="pageimages|coordinates|pageprops", piprop="name", pilicense="free", ppprop="disambiguation|wikibase_item")

def find(stop):
    """Vrátí (článek, soubor na Commons) s fotkou místa, nebo None."""
    name = stop["n"].strip()
    country = COUNTRY_EN.get(stop.get("c"), stop.get("c") or "")
    queries = [  # 1) článek podle názvu (i „Název, Země“), 2) fulltext, 3) nejbližší články kolem bodu na mapě
        ("en", dict(titles=f"{name}|{name}, {country}", redirects=1)),
        ("es", dict(titles=f"{name}|{name}, {country}", redirects=1)),
        ("cs", dict(titles=name, redirects=1)),
        ("en", dict(generator="search", gsrsearch=f"{name} {country}", gsrlimit=10)),
        ("es", dict(generator="search", gsrsearch=f"{name} {country}", gsrlimit=10)),
        ("en", dict(generator="geosearch", ggscoord=f"{stop['lat']}|{stop['lon']}", ggsradius=10000, ggslimit=20)),
    ]
    for lang, q in queries:
        try:
            pages = api(f"{lang}.wikipedia.org", **q, **PROPS).get("query", {}).get("pages")
        except Exception as e:
            print(f"  {lang}: {e}")
            continue
        for p in near(pages, stop)[:3]:
            f = image_of(p)
            if f:
                return p, f
    return None

def clean(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()

def fetch_photo(page, fname, stop):
    r = api("commons.wikimedia.org", titles="File:" + fname, prop="imageinfo", iiprop="url|extmetadata", iiurlwidth=WIDTH)
    info = r["query"]["pages"][0]["imageinfo"][0]
    meta = info.get("extmetadata") or {}
    url = info.get("thumburl") or info["url"]
    data = get(url)
    ext = ".png" if urllib.parse.urlsplit(url).path.lower().endswith(".png") else ".jpg"
    path = f"{DIR}/{slug(stop['n'])}{ext}"
    os.makedirs(DIR, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    return {
        "name": stop["n"],
        "img": path,
        "article": page["title"],
        "file": fname.replace("_", " "),
        "author": clean(meta.get("Artist", {}).get("value"))[:120] or "neuveden",
        "license": clean(meta.get("LicenseShortName", {}).get("value")) or "volná licence",
        "page": info.get("descriptionurl", ""),
        "found": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

def main():
    state = json.load(open("state.json", encoding="utf-8"))
    try:
        idx = json.load(open(INDEX, encoding="utf-8"))
    except Exception:
        idx = {}
    today = datetime.now(timezone.utc).date()
    changed = False
    for s in state.get("stops", []):
        k = norm(s.get("n"))
        if not k or k in BUILTIN or "lat" not in s or "lon" not in s:
            continue
        e = idx.get(k)
        if e and e.get("img") and os.path.exists(e["img"]):
            continue
        if e and e.get("none") and (today - datetime.strptime(e["tried"], "%Y-%m-%d").date()) < timedelta(days=RETRY_DAYS):
            continue
        print(f"Hledám fotku: {s['n']} ({s.get('c', '')})")
        try:
            hit = find(s)
            if hit:
                idx[k] = fetch_photo(*hit, s)
                print(f"  -> {idx[k]['article']}: {idx[k]['file']} ({idx[k]['license']})")
            else:
                idx[k] = {"name": s["n"], "none": True, "tried": today.isoformat()}
                print("  -> nic vhodného nenalezeno")
            changed = True
        except Exception as ex:
            print(f"  chyba: {ex}")
    if changed:
        with open(INDEX, "w", encoding="utf-8") as f:
            json.dump(idx, f, ensure_ascii=False, indent=1, sort_keys=True)
            f.write("\n")
    print("Hotovo." if changed else "Nic nového.")

if __name__ == "__main__":
    main()
