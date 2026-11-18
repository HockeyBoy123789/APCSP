# Unit 6 · Lesson 8 — Loops Make (Lock Screen Maker app)

**Lesson:** Loops Make — build an app that uses loops to change 20 icons at once.
**Source video:** [Code.org Lesson 8 Loops Lock Screen Maker App | Tutorial with Answers](https://youtu.be/B-yYUaC5GxE) — Mr. Kaiser.
**Code appears at:** ~10:00 (event handlers), ~21:40 (`changeColors`), ~23:20 (`changeShapes` and `changeLocations`).

## What the app does

- The lock screen holds **20 icon elements** (`icon0` … `icon19`).
- **Shapes!** picks a random icon from a list and applies it to all 20 with a `for` loop.
- **Colors!** generates a random RGB colour for each icon with a `for` loop, then tints
  the screen background.
- **Locations!** moves each icon to a random x/y position with a `for` loop.

This is the lesson's core idea: one loop over `icon0…icon19` replaces 20 separate
`setProperty` calls.

## Design elements to create in App Lab

| Element ID | Type | Purpose |
|---|---|---|
| `homeScreen` | screen | the lock screen; gets the background colour |
| `shapesButton` | button | randomises the icon |
| `locationsButton` | button | randomises positions |
| `colorsButton` | button | randomises colours |
| `icon0` … `icon19` | image × 20 | the icons being changed |

The icons must be named exactly `icon0` through `icon19` — the code builds the IDs
with `"icon" + i`.

## The code

See [`app.js`](app.js). Key ideas:

- `iconsList` is the pool of icons; `iconIndex` remembers the previous choice.
- `randomNumber(0, iconsList.length - 1)` picks a valid index; the `while` loop forces a
  *different* shape each press.
- All three `change…` functions use `for (var i = 0; i < 20; i++)`, the pattern the
  lesson is teaching.

## Caveats

- Reconstructed from one walkthrough video; your level's starter project may use
  different element IDs or a different number of icons.
- `changeLocations` uses random x/y inside the phone screen (x 50–270, y 50–400).
  Adjust the ranges if your screen is a different size.
- Reference only — submit your own work for graded assignments.
