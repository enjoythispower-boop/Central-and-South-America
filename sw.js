/* Offline režim: zkusí síť, ale když neodpoví do 3 s (slabý signál), vrátí uloženou verzi a síť ji na pozadí obnoví.
   Ukládá se bez ?t=…, aby každá kontrola dat nepřidávala do mezipaměti další kopii souboru. */
const C='cesta-v4',WAIT=3000;
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>clients.claim())));
self.addEventListener('fetch',e=>{
  const r=e.request,u=new URL(r.url);
  if(r.method!=='GET'||u.origin!==location.origin)return;
  const key=u.origin+u.pathname;
  const cached=()=>caches.match(key).then(m=>m||(r.mode==='navigate'?caches.match('./'):undefined));
  const net=fetch(r).then(res=>{if(res.ok){const cp=res.clone();caches.open(C).then(c=>c.put(key,cp))}return res});
  e.waitUntil(net.catch(()=>{}));
  e.respondWith(new Promise(ok=>{
    let done=false;const fin=x=>{if(!done&&x){done=true;ok(x)}};
    const t=setTimeout(()=>cached().then(fin),WAIT);
    net.then(res=>{clearTimeout(t);fin(res)}).catch(()=>{clearTimeout(t);cached().then(m=>{fin(m);if(!done)ok(Response.error())})});
  }));
});
