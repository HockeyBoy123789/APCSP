// Unit 6, Lesson 4 — Lists Make: RemindMe app
// Reconstructed from the answer-key video:
//   "Code.org Lesson 4 Lists Make a Reminder App | Tutorial with Answers"
//   Mr. Kaiser — https://youtu.be/z_OOZ2gaY-s
// Code is fully visible around 15:00–16:40 in that video.
//
// App Lab text mode. Required design elements:
//   reminderInput   text input     (the "New reminder" box)
//   addButton       button         ("Add")
//   reminderOutput  label / text   (the reminder currently shown)
//   countOutput     label / text   (the "n of total" counter)
//   leftButton      button         ("<<")
//   rightButton     button         (">>")

// The list holds every reminder the user has entered, in order.
var inputList = [];

// Which reminder is currently shown. 0 = first reminder.
var index = 0;

// Add the text in the input box to the list, then refresh the screen.
onEvent("addButton", "click", function() {
  appendItem(inputList, getText("reminderInput"));
  setProperty("reminderInput", "text", ""); // clear the input box
  updateScreen();
});

// Draw the current reminder and its position. Called after every change so the
// screen always matches the list and index.
function updateScreen() {
  if (inputList.length < 1) {
    setProperty("reminderOutput", "text", "Add reminders!");
  } else {
    setProperty("reminderOutput", "text", inputList[index]);
    setProperty("countOutput", "text", index + 1);
  }
}

// Move one reminder back, but never past the first item.
onEvent("leftButton", "click", function() {
  if (index > 0) {
    index = index - 1;
    updateScreen();
  }
});

// Move one reminder forward, but never past the last item.
onEvent("rightButton", "click", function() {
  if (index < inputList.length - 1) {
    index = index + 1;
    updateScreen();
  }
});
