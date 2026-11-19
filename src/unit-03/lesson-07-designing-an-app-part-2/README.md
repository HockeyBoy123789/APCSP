# Unit 3 · Lesson 7 — Project: Designing an App, Part 2

**Lesson:** Project — Designing an App, Part 2. Build and finish the multi-screen
"Coding Quiz" app.
**Source video:** [Code.org Lesson 7 Project Designing an App Part 2 | Answer Tutorial | Unit 3 CS Principles](https://youtu.be/ItucouYL8y4) — Mr. Kaiser.
**Code appears at:** ~12:20–14:20 (finished four-question quiz). The walkthrough video
also shows the earlier two-question version and the project's later parts, so the
Code.org header changes from Part 3 to Part 4 to Part 5 as it goes.

## What the app does

1. The home screen has a **Start** button.
2. Each question screen shows four language logos as buttons.
3. A correct answer advances to the next question; a wrong answer jumps to the lose screen.
4. Question 4's correct answer goes to the win screen.
5. The win and lose screens have a **Play Again** button that returns home and plays
   a win/failure sound.

Correct answers in this walkthrough:

| Question | Correct button | Goes to |
|---|---|---|
| 1 | `q1CppBtn` (C++) | `q2Screen` |
| 2 | `q2PyBtn` (Python) | `q3Screen` |
| 3 | `q3JavaBtn` (Java) | `q4Screen` |
| 4 | `q4JSBtn` (JavaScript) | `winScreen` |

## Design elements to create in App Lab

| Element ID | Type | Purpose |
|---|---|---|
| `startBtn` | button | starts the quiz |
| `q1CppBtn` … `q1JSBtn` | buttons | question 1 answers |
| `q2VBBtn` … `q2JSBtn` | buttons | question 2 answers |
| `q3VBBtn` … `q3JSBtn` | buttons | question 3 answers |
| `q4CppBtn` … `q4JSBtn` | buttons | question 4 answers |
| `winPlayAgainBtn` | button | return from the win screen |
| `losePlayAgain` | button | return from the lose screen |

Create seven screens with these exact IDs: `homeScreen`, `q1Screen`, `q2Screen`,
`q3Screen`, `q4Screen`, `winScreen`, `loseScreen`. The language logos are decorative
images; the code only uses the button IDs.

## The code

See [`app.js`](app.js). Key ideas:

- Each `onEvent(..., "click", ...)` handles one button.
- `setScreen` switches between the seven screens.
- `playSound` plays the startup, win, and failure sounds.
- There is no counter or list: the quiz is a **state machine** made of screens and
  button handlers. The current screen *is* the state.

## Caveats

- Reconstructed from one walkthrough video. Your level's screens or button IDs may
  differ — match the IDs in the Design tab.
- The video builds the quiz in stages (two questions, then more). `app.js` is the
  final four-question version.
- The sound URLs are App Lab's built-in sound library paths.
- Reference only — submit your own work for graded assignments.
