---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Surface brief: whole app (index.html)

Mode: Operate (a working trip tracker; the reading and planning tabs inside it follow the same shell).

Audience, job, constraints: the traveller on a phone on the road and in a hostel at night, plus family following from home. Czech UI, static hosting, no backend, no AI, offline-capable. All existing tabs, data, edit mode and behaviour stay; only the visual layer and layout change. The left side rail is removed.

User-pinned direction (beats the roll, 2026-10-22): match a Dribbble travel-app reference closely: dark glassmorphism over blurred warm photographs, frosted circular icon buttons, framed photo cards with chips over the photo, pill tabs whose active state glows peach, dark map with a white route and pink pins under a glass sheet with a grab handle, solid dark bottom tab bar with icon + label, a glass composer with a pink-orange gradient send button. Dark only; the previous light pastel world is discarded.

## Direction contract

THESIS: the app lives inside the light of the current city: its photograph, blurred to a warm peach/rose/amber glow, is the ground under every screen, and all controls are frosted glass laid over it. Refuses the light card-on-flat-ground tracker and the side-rail dashboard.

OWN-WORLD: near-black ground #0C0A0E under a fixed, heavily blurred photo of the current stop with peach (#F4A98A), rose (#E2789A) and amber glows; glass panels white 7-12% with a 1px white 14% rim and inner top highlight; text #F7F2EF, muted #B9AFAD; accent is the pink-orange gradient (#FF8A5B -> #FF4F9A) used only for "now" and the primary send/save action; done is white, next is grey. Figtree throughout, semibold titles, sentence case. Radii 30/24/18 and pills; photo cards sit in a 4px glass frame.

STORY: the visitor sees where the traveller is now, what is next and whether anything on the route needs attention in one screen, then drills into route, timeline, countries, weather and news.

FIRST VIEWPORT: mobile 390. Header row: large title "Přehled" left, three 44px glass circle buttons right (map, weather, alerts with dot). Then the current-stop hero: a framed 4:5 photo card with two stacked glass card edges behind it, chips over the photo (country flag, "Teď tady"), below it the city name 28px semibold + "Zastávka 8 z 11" right, pin row with country, progress line. Then pill chips and a horizontal rail of framed stop cards. Solid dark tab bar at the bottom (Přehled, Trasa, Osa, Země, Více).

FORM: Operate shell, standard controls; top header with glass icon buttons, bottom tab bar on all widths (centered dock on desktop). Signature move: the route screen as a full dark map with the stop list in a glass bottom sheet with a grab handle. seed: none (user-pinned direction, no roll).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Unresolved
- Light theme removed; the settings theme switch goes with it.
- No ratings exist in the data; rating chips from the reference become honest chips (stop number, date, status).
