---
name: Cancún → Buenos Aires
description: A personal overland trip tracker that lives inside the warm, blurred light of the current stop.
colors:
  night-ground: "#0C0A0E"
  bone-text: "#F7F2EF"
  ash-muted: "#BCB1AE"
  smoke-muted: "#91878A"
  peach-glow: "#FFB08F"
  rose-glow: "#E2789A"
  ember-amber: "#B9694C"
  grad-ember: "#FF9A5C"
  grad-fuchsia: "#FF4F9A"
  now-pink: "#FF6A88"
  now-pink-text: "#FF9AAE"
  done-white: "#FFFFFF"
  next-grey: "#6E6569"
  ok-mint: "#7FDDB0"
  warn-honey: "#F6BE63"
  bad-coral: "#FF7272"
  cool-sky: "#8EC5FF"
  peach-ink: "#1B0E0A"
  glass-fill: "rgba(255,255,255,0.07)"
  glass-rim: "rgba(255,255,255,0.14)"
  glass-rim-strong: "rgba(255,255,255,0.26)"
  hairline: "rgba(255,255,255,0.1)"
  map-sea: "#0E0C11"
  map-land: "#211C23"
  map-land-stroke: "#3D343E"
  tint-0: "#2B2328"
  tint-1: "#22262F"
  tint-2: "#2E2A20"
  tint-3: "#30231F"
  tint-4: "#28243A"
  tint-5: "#33212A"
  tint-6: "#25291F"
typography:
  display:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.8rem, 6.4vw, 2.6rem)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.75rem, 5.4vw, 2.3rem)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  title-sm:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1.06rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  body:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  label:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 500
    lineHeight: 1.4
  figure:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "2.8rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.03em"
rounded:
  sm: "12px"
  md: "18px"
  lg: "24px"
  photo-card: "26px"
  xl: "30px"
  pill: "99px"
  circle: "50%"
spacing:
  xs: "6px"
  sm: "8px"
  md: "14px"
  lg: "18px"
  section: "28px"
  gutter-mobile: "16px"
  gutter-desktop: "32px"
components:
  button-glass:
    backgroundColor: "rgba(255,255,255,0.08)"
    textColor: "{colors.bone-text}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "10px 18px"
    height: "44px"
  button-glass-hover:
    backgroundColor: "rgba(255,255,255,0.15)"
  button-primary:
    backgroundColor: "linear-gradient(120deg, rgba(255,154,92,0.32), rgba(255,79,154,0.26))"
    textColor: "#FFF1EA"
    rounded: "{rounded.pill}"
    padding: "10px 18px"
    height: "44px"
  button-send:
    backgroundColor: "linear-gradient(120deg, {colors.grad-ember}, {colors.grad-fuchsia})"
    textColor: "{colors.done-white}"
    rounded: "{rounded.circle}"
    size: "42px"
  button-fab:
    backgroundColor: "linear-gradient(120deg, {colors.grad-ember}, {colors.grad-fuchsia})"
    textColor: "{colors.done-white}"
    rounded: "{rounded.pill}"
    padding: "13px 22px"
    height: "48px"
  icon-button:
    backgroundColor: "rgba(255,255,255,0.08)"
    textColor: "{colors.bone-text}"
    rounded: "{rounded.circle}"
    size: "46px"
  icon-button-sm:
    size: "38px"
  chip:
    backgroundColor: "{colors.glass-fill}"
    textColor: "{colors.bone-text}"
    rounded: "{rounded.pill}"
    padding: "8px 16px"
    height: "40px"
  chip-active:
    backgroundColor: "linear-gradient(120deg, rgba(255,154,92,0.34), rgba(255,120,140,0.2))"
    textColor: "#FFF3EC"
  photo-chip:
    backgroundColor: "rgba(20,14,18,0.35)"
    textColor: "{colors.done-white}"
    rounded: "{rounded.pill}"
    padding: "5px 12px 5px 6px"
  card-glass:
    backgroundColor: "linear-gradient(180deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05))"
    textColor: "{colors.bone-text}"
    rounded: "{rounded.lg}"
    padding: "18px"
  photo-frame:
    backgroundColor: "linear-gradient(180deg, rgba(255,255,255,0.2), rgba(255,255,255,0.07))"
    rounded: "{rounded.xl}"
    padding: "5px"
  photo-card:
    backgroundColor: "linear-gradient(180deg, rgba(255,255,255,0.18), rgba(255,255,255,0.06))"
    textColor: "{colors.done-white}"
    rounded: "{rounded.photo-card}"
    padding: "4px"
    width: "168px"
  input:
    backgroundColor: "rgba(255,255,255,0.06)"
    textColor: "{colors.bone-text}"
    rounded: "{rounded.md}"
    padding: "12px 14px"
  route-sheet:
    backgroundColor: "linear-gradient(180deg, rgba(60,44,52,0.55), rgba(26,20,26,0.72))"
    rounded: "{rounded.xl}"
    padding: "12px 16px 20px"
  tab-bar:
    backgroundColor: "rgba(14,11,15,0.86)"
    textColor: "{colors.smoke-muted}"
    padding: "8px"
  tab-bar-active:
    textColor: "{colors.done-white}"
---

# Design System: Cancún → Buenos Aires

## Overview

**Creative North Star: "Inside the City's Light"**

The app lives inside the light of wherever the traveller is right now. The current stop's photograph is laid behind every screen, blurred past recognition (64px), graded toward peach, rose and amber, and darkened to near-black at the bottom; every control sits on top of it as frosted glass. Change the stop and the whole app's ambient light changes with it. The ground is never a flat colour and never a light page.

Density is phone-first and calm: one column of glass panels, generous pill controls at 40-46px, large semibold titles in sentence case, and photographs carried in thin glass frames rather than bled to the edge. Colour is almost entirely the photograph's; the interface itself is white text, translucent white glass and one warm gradient that marks the present moment. The route reads in three states only: white for where the traveller has been, pink for where they are, grey for what is ahead.

The world is dark only. The earlier light sage/pastel world and its theme switch are discarded and must not return as an alternate mode.

**Key Characteristics:**
- Fixed, heavily blurred, warm-graded photo of the current stop as the ground of every screen.
- Frosted glass panels and circular glass icon buttons with a 1px white rim and an inner top highlight.
- Photographs in a 4-5px glass frame; hero photos carry two stacked glass card edges behind them.
- Pill tabs and chips; the active pill is a peach gradient tint with a peach outline.
- One pink-orange gradient, spent on "now", the primary send/save action and progress fills.
- Done = white, now = pink, next = grey, everywhere the route appears.
- Figtree only, semibold titles, sentence case, Czech copy.

## Colors

A near-black ground lit by a warm photographic glow, white glass and text on top, and a single pink-orange gradient for the present moment.

### Primary
- **Ember-to-Fuchsia Gradient** (`linear-gradient(120deg, {grad-ember}, {grad-fuchsia})`): the one saturated voice. Fills the composer send button, the floating save/action button, the "now" status chip on a photo card, the "now" timeline node, the "jsem tady" inline marker, and progress/budget bar fills. The composer's border is the same gradient at 70-80% strength.
- **Now Pink** (now-pink): the current stop as a point: the map pin and its pulsing halo, the notification badge dot on icon buttons, calendar event dots, the current-stop dot after a chip label, and the budget-limit line in charts. Now Pink Text is its legible text variant on glass.

### Secondary
- **Peach Glow** (peach-glow): the interactive warm accent. Focus rings, active-chip outline, input focus border and halo, links, text caret, selection highlight, "today" outline in the calendar, the weather icon tint, info-severity tags, and the soft tint (16% alpha) behind hint boxes and news icons. Text placed on solid peach or the gradient uses Peach Ink (peach-ink).
- **Rose Glow** (rose-glow) and **Ember Amber** (ember-amber): ambient light only. Together with Peach Glow they form the colour-blend wash and radial glows over the blurred photo. They never fill a control.

### Tertiary
- **Ok Mint** (ok-mint), **Warn Honey** (warn-honey), **Bad Coral** (bad-coral): status only, each with a 16% soft fill for tags, alert panels, severity tiles and news icons. Warn and Bad also recolour progress fills when a budget is close or over.
- **Cool Sky** (cool-sky): the second event marker in the calendar (alongside Now Pink); not used elsewhere.

### Neutral
- **Night Ground** (night-ground): the page, the theme colour, the ring around timeline nodes, and the darkening gradient under the ambient photo.
- **Bone Text** (bone-text): primary text and icons. **Ash Muted** (ash-muted): secondary text, labels, metadata. **Smoke Muted** (smoke-muted): placeholders and inactive tab-bar items.
- **Done White** (done-white) and **Next Grey** (next-grey): visited and upcoming stops on the map, timeline, legend and rail.
- **Glass Fill / Glass Rim / Glass Rim Strong / Hairline**: translucent white at 7%, 14%, 26% and 10%. Fills run 5-12% depending on the surface; the rim strengthens to 26% on hover; hairlines divide list rows and facts.
- **Map Sea, Map Land, Map Land Stroke**: the dark cartography. Visited, current and planned countries step up from the land fill (#2B242D planned, #3A3236 done, #4A2A36 now).
- **Country tints** (tint-0 to tint-6): dark per-country placeholders shown inside a photo frame before or without an image.

### Named Rules
**The One Glow Rule.** The full-strength pink-orange gradient marks only the present moment (now), the primary send/save action and progress fills. Selected tabs and the primary text button use a translucent peach tint of it, never the solid gradient.

**The Three States Rule.** Every representation of the route uses exactly three states: done is white, now is pink, next is grey. No other colour carries route progress.

**The Photo Is the Light Rule.** Warmth comes from the blurred photograph and its peach/rose/amber wash, not from coloured panels. Surfaces stay translucent white over it.

## Typography

**Display Font:** Figtree (self-hosted variable woff2, weights 400-800, Latin and Latin Extended subsets), falling back to system-ui, -apple-system, Segoe UI, Roboto, sans-serif
**Body Font:** Figtree (same file)

**Character:** One friendly geometric sans at two weights does all the work: semibold for anything that names a place or a section, regular and medium for everything else. Tight negative tracking on large titles keeps them compact against busy photographs.

### Hierarchy
- **Display** (600, clamp(1.8rem, 6.4vw, 2.6rem), 1.05, -0.025em): the current-stop city name under the hero photo and the country name on the country hero.
- **Headline** (600, clamp(1.75rem, 5.4vw, 2.3rem), 1.05, -0.025em): the screen title at top left of every view ("Přehled", "Trasa"). Stop detail titles sit just below at 1.5rem.
- **Title** (600, 1.2rem, -0.01em): section headings with a muted text action on the right.
- **Title small** (600, 1.06rem): card headings; photo-card names at 1.02rem; news headlines at 0.96rem.
- **Body** (400, 15px, 1.5, tabular numerals): running text; descriptive paragraphs cap at 62ch in a slightly warmer off-white (#E6DCD8).
- **Label** (500, 0.78rem): field labels, pills, metadata; tags drop to 0.72rem at 600; tab-bar labels are 0.72rem at 500.
- **Figure** (600, 2.8rem, 1, -0.03em): the current temperature; severity counts use 1.7rem at 600.

### Named Rules
**The Sentence Case Rule.** All interface text is Czech in sentence case. The only uppercase, letter-spaced text (0.06em) is country names drawn on the map, as cartographic labels.

**The One Family Rule.** Figtree is the only typeface. Hierarchy comes from size and the 600/500/400 weights, not from a second face.

## Layout

A single centred column (max 1200px) with 16px gutters on mobile (plus the top safe-area inset) and 32px on desktop, bottom padding of 140-150px so content clears the tab bar. Every view opens with a header row: the headline on the left, a group of circular glass icon buttons on the right (8px apart), minimum 48px tall.

Rhythm: 8px between pills, chips and buttons; 14px between stacked cards and grid cells; 18px card padding; 28px above a section heading. Two-column card grids appear from 900px. Horizontal rails of photo cards bleed to the screen edge on mobile (negative 16px margins with scroll-snap) and sit within the column on desktop.

The overview hero stacks photo above metadata on mobile (frame aspect 4:4.3, max 560px tall) and becomes a two-column split (1.25fr photo at 16:11, 1fr metadata bottom-aligned, 32px gap) from 900px.

The route screen is the signature layout. Below 900px the dark map runs edge to edge at min(64vh, 560px) with the header floating over it, and a glass sheet with a grab handle overlaps its bottom by 36px, rounded only at the top. From 900px the map is fixed full-screen behind everything and the stop list becomes a floating glass panel on the right (min(480px, 42vw), scrolls internally), with zoom controls and legend at the left.

Navigation is a solid dark tab bar pinned to the bottom on mobile and a centred floating dock (18px above the bottom edge) on desktop.

## Elevation & Depth

Depth is frosted glass, not shadow. Surfaces separate from the photograph through backdrop blur (22px, saturate 150%; 24-30px on the tab bar, route sheet, menu sheet and lightbox), a translucent white fill that is lighter at the top, a 1px white rim, and a 1px inner top highlight. A single soft, deep drop shadow sits under floating glass so it reads above the glow, never as an outline. Where backdrop-filter is unsupported, cards and the route sheet fall back to an opaque dark plum (rgba(34,27,33,0.94)).

### Shadow Vocabulary
- **Lift** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 22px 44px -24px rgba(0,0,0,.75)`): glass cards, photo frames and photo cards.
- **Icon highlight** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.12)`): circular glass icon buttons.
- **Active pill** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 6px 16px -10px rgba(0,0,0,.55)`): the selected chip or tab.
- **Sheet** (`box-shadow: 0 -20px 40px -24px rgba(0,0,0,.8)`): the route sheet, shadowing upward onto the map.
- **Floating** (`box-shadow: 0 24px 50px -16px rgba(0,0,0,.85)`): the desktop dock and the "more" menu sheet.
- **Now ring** (`box-shadow: var(--lift), 0 0 0 1px rgba(255,140,120,.35)`): the current stop's photo card, with a peach border.

### Named Rules
**The Frosted Not Shadowed Rule.** A surface earns its layer from blur, rim and inner highlight. Shadows are soft, negative-spread and below the element; never a hard offset, never a coloured glow.

## Shapes

Generous, nested curves. The radius scale is 30px for photo frames, hero stacks, the map and sheets; 24px for glass cards, alerts and news cards; 18px for inputs, hints and menu tiles; 12px for calendar days; 26px (outer) / 22px (inner) for rail photo cards; and fully round for every button, chip, tab and pill. Icon buttons, the send button, news icons and timeline nodes are circles.

Photographs are always clipped inside a glass frame: a 4-5px translucent white gradient band with a 1px rim, the image corner equal to the frame radius minus the band. Hero and detail photos add two glass card edges peeking above the frame (inset 7% and 3.5%, 7px apart). Gallery thumbnails and the lightbox use a 4-5px 10-12% white border as the same frame.

**The Nested Radius Rule.** An inner photo's corner radius is its frame's radius minus the frame's padding, so the band reads even all the way round.

## Components

### Buttons
Soft, round and glassy; the gradient appears only where an action creates something.
- **Shape:** full pill (99px), 44px minimum height (38px small).
- **Glass (default):** 8% white fill, 1px glass rim, backdrop blur, medium 0.88rem label, icon + label 8px apart. Hover lifts the fill to 15% and the rim to 26%; press scales to 0.97.
- **Primary:** a translucent ember-to-fuchsia tint (32%/26%) with a 70% peach outline and warm white label; hover deepens the tint.
- **Send:** a 42px circle filled with the full gradient, white arrow icon; press scales to 0.92. Lives inside the composer.
- **Floating action:** a gradient pill (13px 22px, 48px tall) bottom right above the tab bar; disabled turns to dark glass with muted text.
- **Destructive:** glass with coral text and a 35% coral outline.

### Icon buttons
- 46px glass circles (38px small) with a 1px rim and inner top highlight, 20px stroked line icons (1.8 stroke). An 8px Now Pink dot marks unread alerts. Hover 16% fill, press 0.94.

### Chips
- **Style:** 40px glass pills, 8px 16px, medium 0.86rem, horizontally scrolling rows with hidden scrollbars. Used for view tabs (segmented) and filters alike.
- **State:** active = peach-to-pink translucent gradient fill, 80% peach outline, warm white text and the active-pill shadow. A chip for the current country carries a trailing 7px Now Pink dot.
- **Photo chips:** dark glass (35% plum) with a 22% white rim, white 0.8rem text, sitting over photos at the top corners (flag + country, "Teď tady", stop number).
- **Status pills and stats:** smaller 8% glass pills (0.78-0.8rem); tags are tinted with the 16% status soft fills.

### Cards / Containers
- **Corner Style:** 24px.
- **Background:** vertical white glass gradient (10% to 5%) with backdrop blur.
- **Shadow Strategy:** Lift (see Elevation).
- **Border:** 1px glass rim.
- **Internal Padding:** 18px (14-16px in timeline and news cards).

### Photo cards
Framed portrait cards (168px wide, 140px in the stop rail, aspect 3:3.9) in a 4px glass band. The photo darkens toward the bottom (82%) for the white name and date, a stop-number chip sits top left and a status chip top right. Done cards desaturate the photo slightly; the current card gets a peach border, the now ring and a gradient status chip; a selected card gets a white border with a 2px white halo. Hover lifts 3px.

### Inputs / Fields
- **Style:** 6% white fill, 1px glass rim, 18px radius, 12px 14px padding, peach caret, smoke-grey placeholder.
- **Focus:** border turns 75% peach, fill rises to 9%, plus a 3px peach halo at 16%.
- **Composer:** a 24px dark glass field whose 1.5px border is the gradient, holding a borderless textarea and the gradient send button.

### Navigation
- **Mobile:** a solid dark bar (86% near-black, 24px blur, hairline top border) with five icon + label items (Přehled, Trasa, Osa, Země, Více), labels 0.72rem medium. Inactive items are smoke grey, hover is bone, active is white with a heavier icon stroke (2.2). "Více" opens a glass sheet of 18px tiles in a three-column grid.
- **Desktop (861px and up):** the same bar becomes a centred floating dock, 26px radius, 1px rim, the floating shadow, 76px items, with desktop-only items replacing the "Více" sheet.

### Route map and sheet
A dark map (sea #0E0C11, land #211C23) with the travelled route as a solid 3px white line, the full route as a dotted 45% white line, numbered pins coloured by the Three States Rule, and a pulsing Now Pink halo on the current pin (static under reduced motion). The stop list sits in a glass sheet with a 44px by 5px grab handle at 40% white. A small dark-glass pill legend and glass zoom buttons float over the map.

### Timeline
A 1px rim-coloured spine with 13px nodes ringed in Night Ground; done/next nodes take their state colour, the now node takes the gradient with an extra 25% pink ring. Each entry is a glass card.

## Do's and Don'ts

### Do:
- **Do** put the current stop's photo, blurred (64px) and warm-graded, behind every screen, fading to Night Ground (#0C0A0E) at the bottom.
- **Do** build every surface from translucent white glass: 5-12% fill, 1px 14% rim, inner top highlight, 22px backdrop blur, with an opaque dark fallback where blur is unsupported.
- **Do** frame every photograph in a 4-5px glass band and nest its radius (frame radius minus band).
- **Do** mark selection on pills with the translucent peach gradient and peach outline.
- **Do** keep route state to white (done), pink (now), grey (next) on map, timeline, legend and cards.
- **Do** keep touch targets at 40px or more (44px for buttons, 46px icon buttons) and the 2px peach focus ring with 3px offset.
- **Do** respect reduced motion: no view rise animation, no pin pulse, no hover lifts or press scaling.

### Don't:
- **Don't** reintroduce a light theme or a theme switch; the world is dark only.
- **Don't** use the full-strength pink-orange gradient for anything but now, the primary send/save action and progress fills.
- **Don't** place opaque solid panels over the ambient photo, except the dark tab bar and the no-blur fallback.
- **Don't** use hard offset shadows or coloured glows; depth is blur, rim and soft dark drop.
- **Don't** add a second typeface or uppercase tracked labels in the interface; uppercase is reserved for country names on the map.
- **Don't** bleed photographs edge to edge in content views; they sit in a glass frame (the full-screen map is not a photograph).
- **Don't** bring back a side rail; navigation is the bottom tab bar on mobile and the centred dock on desktop.
