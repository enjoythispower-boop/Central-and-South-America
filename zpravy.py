#!/usr/bin/env python3
"""Bezplatný zpravodajský skript (bez AI a bez API klíčů). Jednou denně stáhne data z veřejných zdrojů
a zapíše upozornění k zemím na trase do news.json.
Zdroje: USGS (zemětřesení), GDACS (cyklóny, záplavy, sopky, požáry), GDELT (zprávy o protestech a blokádách).
Používá jen standardní knihovnu Pythonu."""
import json, math, re, sys, time, unicodedata, urllib.parse, urllib.request
from datetime import datetime, timezone, timedelta

UA = {"User-Agent": "cesta-zpravy/1.0 (osobni cestovni stranka)"}
MAX_ITEMS = 60
TTL = {"eq": 3, "tc": 4, "fl": 4, "vo": 4, "wf": 4, "news": 5}  # po kolika dnech zpráva zmizí (u probíhajících událostí se obnovuje)
ISO3 = {"MEX": "Mexiko", "GTM": "Guatemala", "SLV": "Salvador", "NIC": "Nikaragua", "CRI": "Kostarika", "PAN": "Panama",
        "COL": "Kolumbie", "ECU": "Ekvádor", "PER": "Peru", "BOL": "Bolívie", "CHL": "Chile", "ARG": "Argentina", "PRY": "Paraguay", "URY": "Uruguay"}
EN = {"Mexico": "Mexiko", "Guatemala": "Guatemala", "El Salvador": "Salvador", "Nicaragua": "Nikaragua", "Costa Rica": "Kostarika",
      "Panama": "Panama", "Colombia": "Kolumbie", "Ecuador": "Ekvádor", "Peru": "Peru", "Bolivia": "Bolívie", "Chile": "Chile", "Argentina": "Argentina",
      "Paraguay": "Paraguay", "Uruguay": "Uruguay"}
NAMES = {  # názvy pro hledání zpráv (angl. + špan.)
    "Mexiko": ["Mexico", "México"], "Guatemala": ["Guatemala"], "Salvador": ["El Salvador"], "Nikaragua": ["Nicaragua"],
    "Kostarika": ["Costa Rica"], "Panama": ["Panama", "Panamá"], "Kolumbie": ["Colombia"], "Ekvádor": ["Ecuador"], "Peru": ["Peru", "Perú"],
    "Bolívie": ["Bolivia"], "Chile": ["Chile"], "Argentina": ["Argentina"], "Paraguay": ["Paraguay"], "Uruguay": ["Uruguay"]}
GDACS_TYPES = {"TC": "Tropický cyklón", "FL": "Záplavy", "VO": "Sopečná aktivita", "WF": "Lesní požár"}
LEVEL_CZ = {"Red": "červená", "Orange": "oranžová"}

def get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")

def km(a, b):
    t = math.radians
    dl, dn = t(b[0] - a[0]), t(b[1] - a[1])
    q = math.sin(dl / 2) ** 2 + math.cos(t(a[0])) * math.cos(t(b[0])) * math.sin(dn / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(q))

def addd(iso, n):
    return (datetime.strptime(iso, "%Y-%m-%d") + timedelta(days=n)).strftime("%Y-%m-%d")

def infer(it):
    """Doplní typ a platnost u starších položek bez těchto údajů."""
    t = (it.get("title") or "").lower()
    typ = it.get("type") or ("eq" if t.startswith("zemětřesení") else "tc" if t.startswith("tropick") else "fl" if t.startswith("záplav") else "vo" if t.startswith("sopeč") else "wf" if t.startswith("lesní") else "news")
    it["type"] = typ
    it.setdefault("expires", addd(it.get("date") or datetime.now(timezone.utc).strftime("%Y-%m-%d"), TTL.get(typ, 4)))
    return it

def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")

def load_stops():
    try:
        s = json.load(open("state.json", encoding="utf-8"))
        stops = [x for x in s["stops"] if "lat" in x and "lon" in x]
        cur = next((x for x in stops if x["id"] == s.get("cur")), stops[0] if stops else None)
        return stops, cur
    except Exception:
        return [], None

def nearest(lat, lon, stops):
    best = None
    for s in stops:
        d = km((lat, lon), (s["lat"], s["lon"]))
        if best is None or d < best[0]:
            best = (d, s)
    return best

def dist_text(lat, lon, cur):
    if not cur:
        return ""
    return f" Vzdálenost od tvé aktuální zastávky ({cur['n']}): asi {round(km((lat, lon), (cur['lat'], cur['lon']))/10)*10} km."

# ---------- USGS: zemětřesení ----------
def usgs(stops, cur, today):
    data = json.loads(get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"))
    out = []
    for f in data.get("features", []):
        p, g = f.get("properties", {}), f.get("geometry", {}).get("coordinates", [])
        mag = p.get("mag")
        if mag is None or len(g) < 2 or mag < 5.0:
            continue
        _near = nearest(g[1], g[0], stops)
        lon, lat, depth = g[0], g[1], (g[2] if len(g) > 2 else 0)
        place = p.get("place") or ""
        country = EN.get(place.split(",")[-1].strip())
        near = nearest(lat, lon, stops)
        if not country and near and near[0] <= 250:
            country = near[1].get("c")
        if country not in NAMES:
            continue
        if mag < 5.5 and not (_near and _near[0] <= 250):
            continue  # slabší otřesy daleko od trasy vynecháme
        dcur = km((lat, lon), (cur["lat"], cur["lon"])) if cur else 9999
        sev = "nebezpeci" if (mag >= 6.5 or (mag >= 6.0 and dcur <= 200)) else "pozor" if (mag >= 5.5 or p.get("tsunami")) else "info"
        date = datetime.fromtimestamp(p["time"] / 1000, timezone.utc).strftime("%Y-%m-%d")
        out.append({"country": country, "category": "Přírodní katastrofa", "severity": sev,
                    "title": f"Zemětřesení M{mag:.1f} – {place}"[:120],
                    "summary": f"Zemětřesení o síle M{mag:.1f}, hloubka asi {depth:.0f} km ({place}).{dist_text(lat, lon, cur)}"
                               + (" Bylo vydáno varování před tsunami." if p.get("tsunami") else ""),
                    "date": date, "url": p.get("url") or "", "source": "USGS",
                    "type": "eq", "expires": addd(date, TTL["eq"]), "lat": round(lat, 2), "lon": round(lon, 2)})
    return out

# ---------- GDACS: cyklóny, záplavy, sopky, požáry ----------
def gdacs(stops, cur, today):
    since = (datetime.now(timezone.utc) - timedelta(days=21)).strftime("%Y-%m-%d")
    url = ("https://www.gdacs.org/gdacsapi/api/events/geteventlist/SEARCH?eventlist=TC;FL;VO;WF"
           f"&fromdate={since}&todate={today}&alertlevel=red;orange")
    data = json.loads(get(url))
    out, cutoff = [], datetime.now(timezone.utc) - timedelta(days=4)
    for f in data.get("features", []):
        p, g = f.get("properties", {}), f.get("geometry", {}).get("coordinates", [])
        if len(g) < 2:
            continue
        lon, lat = g[0], g[1]
        iso = [a.get("iso3") for a in p.get("affectedcountries", []) if a.get("iso3")] or [p.get("iso3")]
        country = next((ISO3[i] for i in iso if i in ISO3), None)
        near = nearest(lat, lon, stops)
        if not country and near and near[0] <= 400:
            country = near[1].get("c")
        if country not in NAMES:
            continue
        try:
            end = datetime.fromisoformat(p.get("todate", "")).replace(tzinfo=timezone.utc)
        except Exception:
            end = datetime.now(timezone.utc)
        current = str(p.get("iscurrent", "")).lower() == "true"
        if not current and end < cutoff:
            continue
        level = p.get("alertlevel", "Orange")
        typ = GDACS_TYPES.get(p.get("eventtype"), "Přírodní událost")
        sev_text = (p.get("severitydata") or {}).get("severitytext", "")
        url_rep = (p.get("url") or {}).get("report", "")
        out.append({"country": country, "category": "Přírodní katastrofa", "severity": "nebezpeci" if level == "Red" else "pozor",
                    "title": f"{typ} – {p.get('name') or country}"[:120],
                    "summary": f"{typ}: výstraha GDACS ({LEVEL_CZ.get(level, level)}). {sev_text}.{dist_text(lat, lon, cur)} (text ze zdroje v angličtině)",
                    "date": (p.get("fromdate") or today)[:10], "url": url_rep, "source": "GDACS",
                    "type": p.get("eventtype", "tc").lower(), "ongoing": True, "lat": round(lat, 2), "lon": round(lon, 2),
                    "expires": addd(today if current else end.strftime("%Y-%m-%d"), TTL.get(p.get("eventtype", "tc").lower(), 4))})
    return out

# ---------- GDELT: protesty, blokády, stávky ----------
KEY = re.compile(r"\b(protest\w*|demonstrat\w*|blockad\w*|roadblock\w*|unrest|riot\w*|curfew|state of emergency|clashes|general strike|"
                 r"(?:transport|truck\w*|workers?|teachers?|miners?|bus|national)\s+strikes?|manifestacion\w*|bloqueo\w*|paro nacional|"
                 r"paro de transporte|huelga\w*|toque de queda|estado de emergencia|disturbios|enfrentamientos)\b", re.I)
HEAVY = re.compile(r"blockad|roadblock|curfew|state of emergency|clashes|riot|killed|bloqueo|toque de queda|estado de emergencia|enfrentamientos|disturbios|muert", re.I)
def gdelt(stops, cur, today):
    out = []
    kw = "(protest OR protests OR blockade OR roadblock OR unrest OR curfew OR strike OR protestas OR bloqueos OR huelga OR paro)"
    for cz, names in NAMES.items():
        q = "(" + " OR ".join(f'"{n}"' for n in names) + ") " + kw
        url = "https://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(
            {"query": q, "mode": "artlist", "format": "json", "maxrecords": "40", "timespan": "2d", "sort": "datedesc"})
        arts = None
        for attempt in range(2):
            time.sleep(6)  # GDELT: nejvýše 1 požadavek za 5 s
            try:
                txt = get(url, 40)
                if txt.lstrip().startswith("{"):
                    arts = json.loads(txt).get("articles", []); break
                if "limit requests" in txt:
                    time.sleep(15)
            except Exception as e:
                print(f"GDELT {cz}: {e}", file=sys.stderr)
        if not arts:
            continue
        got, seen_dom = 0, set()
        for a in arts:
            title = (a.get("title") or "").strip()
            lang = (a.get("language") or "").lower()
            if lang not in ("english", "spanish") or not KEY.search(title):
                continue
            if not any(norm(n) in norm(title) for n in names):
                continue
            dom = a.get("domain", "")
            if dom in seen_dom or not a.get("url"):
                continue
            seen_dom.add(dom)
            sd = a.get("seendate", "")
            date = f"{sd[:4]}-{sd[4:6]}-{sd[6:8]}" if re.match(r"^\d{8}T", sd) else today
            if not HEAVY.search(title):
                continue  # běžné protesty bez blokád a nepokojů vynecháváme
            out.append({"country": cz, "category": "Protesty a stávky", "severity": "pozor",
                        "title": title[:120], "summary": f"Zpráva o protestech, blokádách nebo stávce ({'španělsky' if lang == 'spanish' else 'anglicky'}, zdroj {dom}). Otevři zdroj pro podrobnosti.",
                        "date": date, "url": a["url"], "source": dom, "type": "news", "expires": addd(date, TTL["news"])})
            got += 1
            if got >= 2:
                break
    return out

def main():
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    stops, cur = load_stops()
    new, ok = [], 0
    for name, fn in (("USGS", usgs), ("GDACS", gdacs), ("GDELT", gdelt)):
        try:
            items = fn(stops, cur, today)
            new += items; ok += 1
            print(f"{name}: {len(items)} položek")
        except Exception as e:
            print(f"{name} selhal: {e}", file=sys.stderr)
    if ok == 0:
        sys.exit("Žádný zdroj nebyl dostupný.")
    try:
        old = json.load(open("news.json", encoding="utf-8")).get("items", [])
    except Exception:
        old = []
    seen, items = set(), []
    for it in new + [infer(i) for i in old if isinstance(i, dict) and i.get("title")]:
        key = it.get("url") or (it["country"], it["title"].lower())
        if key in seen or it.get("expires", today) < today:
            continue
        seen.add(key); items.append(it)
    items.sort(key=lambda x: x.get("date", ""), reverse=True)
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump({"updated": now.isoformat(timespec="seconds"), "items": items[:MAX_ITEMS]}, f, ensure_ascii=False, indent=1)
    print(f"Hotovo: nových {len(new)}, celkem {min(len(items), MAX_ITEMS)}")

if __name__ == "__main__":
    main()
