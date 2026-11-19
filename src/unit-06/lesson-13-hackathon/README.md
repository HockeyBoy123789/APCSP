# Unit 6 · Lesson 13 — Project: Hackathon

**Lesson:** Project — Hackathon. The multi-day end-of-unit project where you choose a
topic and dataset, then build a multi-screen app that answers a question with data.
**Source video:** [Code.org Hackathon App - Complete Project Tutorial - All Parts | Unit 6 CSP](https://youtu.be/ChYHvfktgCE) — Mr. Kaiser.
**Code appears at:** ~38:40 in text mode (main program, lines 1–38), and the finished
block-mode version at the end of the video (which adds the two Home buttons). The first
frames show the completed app under the title "Lesson 17: Semester Hackathon Part 5".

## What the app does

This is **one example** hackathon project: **AP CS Test Taker Demographics**.

1. The home screen has **Race** and **Gender** buttons.
2. **Gender** opens a screen with a state dropdown. Selecting a state shows what
   percentage of that state's AP CS test takers were female.
3. **Race** opens a screen with its own state dropdown. Selecting a state shows a
   multi-line summary of test takers by race.
4. Each detail screen has a **Home** button.

The lesson does **not** require this exact topic. The point is the pattern: choose a
question, import a table, pull columns into lists, traverse to find the selected row,
and display the result.

## Data table

Import **AP Computer Science Test Taker Demographics by State (2019)** into the Data
tab. The code reads these columns:

| Column | Used for |
|---|---|
| `State` | matching the dropdown selection |
| `Total % female` | gender screen output |
| `Total Black` | race screen output |
| `Total Hispanic/Latino` | race screen output |
| `Total American Indian/Alaska Native` | race screen output |
| `Total Native Hawaiian/Other Pacific Islander` | race screen output |

## Design elements to create in App Lab

| Element ID | Type | Screen | Purpose |
|---|---|---|---|
| `genderBtn` | button | `homeScreen` | open the gender screen |
| `raceBtn` | button | `homeScreen` | open the race screen |
| `genderStatesDropDown` | dropdown | `genderScreen` | choose a state |
| `raceStateDrop` | dropdown | `raceScene` | choose a state |
| `genderOutput` | label / text area | `genderScreen` | percentage output |
| `raceOutput` | label / text area | `raceScene` | multi-line summary |
| `genderHomeBtn` | button | `genderScreen` | back to home |
| `raceHomeBtn` | button | `raceScene` | back to home |

Create the screens with these exact IDs: `homeScreen`, `genderScreen`, `raceScene`.
The home-screen people icon, the race-screen pie/bar chart, and the title labels are
decorative and are not referenced by the code.

## The code

See [`app.js`](app.js). Key ideas:

- `getColumn` turns one table column into a list. All six lists are **parallel**, so
  index `i` refers to the same state in every list.
- Each dropdown handler stores the selected state in `stateSelection`, then uses a
  `for` loop to find the matching index.
- The race handler builds `output` one line at a time with `+=`-style concatenation
  (written as `output = output + ...` here) and calls `setText` once at the end.
- `setScreen` switches between the three screens.

## Suggested order to attempt your own hackathon app

1. Pick a question your dataset can answer, and import the table.
2. Build the home screen with one button per question/screen.
3. Pull the needed columns with `getColumn` and check them in the Debug Console.
4. Build one dropdown handler that finds the selected row.
5. Add the output, then wire up the Home buttons.

## Caveats

- This is an example, not the required hackathon topic. Your app should use your own
  question, dataset, and design.
- Column names are case- and space-sensitive. If `getColumn` returns an empty list,
  open the Data tab and copy the column name exactly.
- The video's first section is the finished Part 5 app; the rest rebuilds it from
  scratch, so timestamps are approximate.
- Reference only — submit your own work for graded assignments.
