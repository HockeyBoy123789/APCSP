# Unit 4 · Lesson 12 — Project: Decision Maker App, Part 2

**Lesson:** Project — Decision Maker App, Part 2. Build the "Fortune Teller" app with
variables, conditionals, and a helper function.
**Source video:** [Code.org Project Decision Maker App Lesson 12 | Tutorial with Answers | Full App](https://youtu.be/OTx-S3ZmGxE) — Mr. Kaiser.
**Code appears at:** ~28:00–30:00 (finished code with all three conditional blocks).

## What the app does

1. You enter your name in a text box.
2. You pick a colour from a dropdown (`red`, `green`, or `blue`).
3. **Up** and **Down** buttons change your age. The age starts at 20.
4. The app combines the name, colour, and age into a fortune in the `mainArea` text area.

The fortune logic is three separate `if` / `else if` chains:

| Colour | Age | Fortune fragment |
|---|---|---|
| `red` | `> 16` | `rosy.` |
| `red` | `<= 16` | `rad!.` |
| `blue` | `> 30` | `awful.` |
| `blue` | `<= 30` | `brilliant.` |
| anything else | `< 10` | `childish.` |
| anything else | `>= 10` | `colorful.` |

## Design elements to create in App Lab

| Element ID | Type | Purpose |
|---|---|---|
| `nameInput` | text input | enter your name |
| `colorDrop` | dropdown | red / green / blue |
| `ageTextArea` | label or text area | shows the current age |
| `upBtn` | button | increase age |
| `downBtn` | button | decrease age |
| `mainArea` | label or text area | shows the fortune |

Match the IDs exactly — the code uses them.

## The code

See [`app.js`](app.js). Key ideas:

- `var age = 20;` sets the starting age, so the screen and variable agree at load.
- `updateScreen()` is a **function** called after every change, so the fortune is
  always rebuilt from the current `username`, `color`, and `age`.
- The three chains are deliberately separate. A red/blue choice only runs the first
  two chains; any other colour falls through to the third chain.
- `myText` is built in two steps so the long concatenation stays readable.

## Caveats

- Reconstructed from one walkthrough video. Your dropdown values may be capitalised
  differently; the comparisons are case-sensitive, so keep them lowercase.
- If your `ageTextArea` starts empty, add `setText("ageTextArea", age);` once at the
  bottom of the file (outside any event) or run the app once to populate it.
- Reference only — submit your own work for graded assignments.
