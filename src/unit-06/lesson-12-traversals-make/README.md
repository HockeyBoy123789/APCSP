# Unit 6 · Lesson 12 — Traversals Make (Random Forecaster app)

**Lesson:** Traversals Make — filter a dataset and pick a random row from it.
**Source video:** [Code.org Lesson 12 Traversals Make a Random Forecaster App | Answer Tutorial](https://youtu.be/pk32rysRQAg) — Mr. Kaiser.
**Code appears at:** ~12:00 (filter loop), ~15:30 (`updateScreen`).

## What the app does

1. Reads six columns out of the **Daily Weather** table with `getColumn`.
2. Builds a **filtered set of parallel lists** containing only tomorrow's rows
   (`Forecast Number == 1`). This is the traversal pattern from the lesson.
3. When **Get Forecast** is clicked, picks a random index in the filtered lists and
   shows that city's high, low, condition and icon.

## Design elements to create in App Lab

| Element ID | Type | Purpose |
|---|---|---|
| `forecastButton` | button | runs `updateScreen` |
| `cityOutput` | label | city name |
| `highTempOutput` | label | high temperature |
| `lowTempOutput` | label | low temperature |
| `conditionOutput` | label | condition text |
| `iconOutput` | image | weather icon |

Also import the **Daily Weather** table into the project's Data tab.

## The code

See [`app.js`](app.js). Key ideas:

- `getColumn` turns a table column into a list.
- The `for` loop **traverses** the whole table; the `if` keeps only tomorrow's rows.
- The five `tomorrow…` lists stay **parallel** — index `n` in each refers to the same
  city.
- `randomNumber(0, tomorrowCities.length - 1)` stays in bounds because all filtered
  lists are the same length.

## Caveats

- Reconstructed from one walkthrough video. If your table uses a different "tomorrow"
  value (for example `0` instead of `1`), change the `if` condition.
- The video builds `updateScreen` and the click handler slightly differently as it
  goes; this is the final working version.
- Reference only — submit your own work for graded assignments.
