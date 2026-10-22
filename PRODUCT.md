# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
The owner, travelling overland from Cancún (Mexico) to Buenos Aires (Argentina), using it mostly on a phone on the road, often with poor connectivity. Family and friends follow along from home to see where the traveller is and what is happening on the route. Audience is Czech-speaking.

## Product Purpose
A personal trip tracker for one long Central and South America route. It holds the itinerary and current stop, a trip log, and daily route alerts for the countries and stops ahead. Success: the traveller can check status and plan the next leg quickly, and followers can see progress without asking.

## Positioning
Built around one specific route and one person's real progress, with route-aware alerts (distance from the current stop) rather than generic country news. Not a general travel planner or map app.

## Operating Context
- Single-page app in `index.html` with a service worker (`sw.js`) for offline use; installable as a PWA.
- Stops and current position live in `state.json`.
- A scheduled GitHub Actions workflow (`zpravy.yml`, daily 05:00 UTC) runs `zpravy.py`, which writes alerts to `news.json` from public sources: USGS (earthquakes), GDACS (cyclones, floods, volcanoes, wildfires), GDELT (protest and blockade news).
- Hosted statically from the GitHub repository.

## Capabilities and Constraints
- UI language is Czech; alert text from sources may remain English and is labelled as such.
- No backend, no paid services, no AI and no API keys. Python standard library only for the news script.
- Must work offline from cache after first load.
- Mobile-first use: bottom tab bar on phones, a centred floating dock on desktop (no sidebar). Dark theme only.
- Multi-language support is not decided.

## Evidence on Hand
Real route data in `state.json`, live alerts in `news.json`, one trip photo in `photos/`. No testimonials or external proof exist; none should be invented.

## Product Principles
- Glanceable on the road: current stop and what matters next come first.
- Honest alerts: show source, date and distance from the current stop; never imply certainty the data lacks.
- Works with bad connectivity: offline first, light on requests.
- Stays free and self-contained: no accounts, no paid dependencies.
- Personal and specific to this route, not a generic travel template.
