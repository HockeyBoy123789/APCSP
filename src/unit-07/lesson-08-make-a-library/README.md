# Unit 7 · Lesson 8 — Project: Make a Library

**Lesson:** Project — Make a Library, Part 1. Write a set of reusable functions over a
dataset and share them as a library.
**Source video:** [Code.org Project Lesson 8 Make a Library | Tutorial with Answers | Full App](https://youtu.be/1joEzBtosrY) — Mr. Kaiser.
**Code appears at:** ~10:00 (top half: `getRandomIndex`, `getName`, `getCerealImage`), ~16:40 (bottom half: `checkCalories`, `allCaloriesCheck`).

## What this file is

A **library**, not an app. In App Lab you create it as a library project, then import
it into another project with **Manage Libraries → Import**. The importing project must
have the **Cereal Nutrition** data table.

## Functions

| Function | Parameters | Returns |
|---|---|---|
| `getRandomIndex()` | — | a random valid row index |
| `getName(index)` | `index` | cereal name at that row |
| `getCerealImage(index)` | `index` | box image at that row |
| `checkCalories(guess, index)` | `guess`, `index` | `true` if the guess matches that row's calories |
| `allCaloriesCheck(guess)` | `guess` | how many cereals match the guess |

## The code

See [`library.js`](library.js). Key ideas from the lesson:

- **Parameters** let one function work for any row (`getName(index)`).
- **Return values** send data back to the calling app.
- `allCaloriesCheck` shows the difference between "check one row" and "traverse the
  whole column with a loop and count matches".
- `getRandomIndex` uses `nameList.length` so the random index can never be out of
  bounds.

## Using the library from an app

```javascript
var index = getRandomIndex();
setText("nameOutput", getName(index));
setProperty("boxOutput", "image", getCerealImage(index));
```

## Caveats

- Reconstructed from one walkthrough video. Column names depend on the imported table
  version — check the Data tab if `getColumn` returns an empty list.
- The video uses the library project's own Data tab while developing; import the table
  into the consuming app as well.
- Reference only — submit your own work for graded assignments.
