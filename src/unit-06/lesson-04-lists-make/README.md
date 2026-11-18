# Unit 6 · Lesson 4 — Lists Make (RemindMe app)

**Lesson:** Lists Make — build the RemindMe app with a list and a counter pattern.
**Source video:** [Code.org Lesson 4 Lists Make a Reminder App | Tutorial with Answers](https://youtu.be/z_OOZ2gaY-s) — Mr. Kaiser.
**Code appears at:** ~15:00–16:40 (finished app runs at ~16:40, then the video submits it).

## What the app does

1. You type a reminder into the text box and press **Add**.
2. The reminder is appended to a list.
3. The app shows one reminder at a time, with a counter (`2` = second reminder).
4. **<<** and **>>** step through the list; they stop at the first and last reminder instead of
   running off the end.

## Design elements to create in App Lab

| Element ID | Type | Purpose |
|---|---|---|
| `reminderInput` | text input | where the new reminder is typed |
| `addButton` | button | adds the reminder |
| `reminderOutput` | label | shows the current reminder |
| `countOutput` | label | shows the current position (1-based) |
| `leftButton` | button | previous reminder |
| `rightButton` | button | next reminder |

Match the IDs exactly — the code uses them.

## The code

See [`app.js`](app.js). Key ideas:

- `inputList` is the list; `index` is a **counter** pointing at the item on screen.
- `appendItem(inputList, getText("reminderInput"))` adds to the end of the list.
- `updateScreen()` is a **function** so the same drawing logic runs after every action.
- The guards `index > 0` and `index < inputList.length - 1` prevent out-of-bounds access.

## Suggested order to attempt it yourself

1. Build the design elements and get **Add** appending to a list.
2. Get the newest reminder to display.
3. Add the counter.
4. Add the left/right buttons, then add the bounds checks last.

## Caveats

- This is the solution shown in one walkthrough video, not Code.org's official answer
  key. Your level may use different element IDs.
- App Lab's block mode creates `var inputList = [];` and `var index = 0;` automatically
  when you use "Create variable"; in text mode the declarations at the top of `app.js`
  do the same job.
- Reference only — submit your own work for graded assignments.
