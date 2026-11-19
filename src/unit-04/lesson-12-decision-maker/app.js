// Unit 4, Lesson 12 — Project: Decision Maker App, Part 2
// "Fortune Teller" — a decision-maker app using variables, conditionals, and a function.
// Reconstructed from the answer-key video:
//   "Code.org Project Decision Maker App Lesson 12 | Tutorial with Answers | Full App"
//   Mr. Kaiser — https://youtu.be/OTx-S3ZmGxE
//
// App Lab text mode. Required design elements:
//   nameInput    text input   (enter your name)
//   colorDrop    dropdown     (red / green / blue)
//   ageTextArea  label/text   (shows the current age)
//   upBtn        button       (age + 1)
//   downBtn      button       (age - 1)
//   mainArea     label/text   (the fortune)

// The user's name, chosen colour, age, and the sentence fragment selected below.
var username;
var color;
var age = 20;
var output;

// Update the name whenever the text input changes.
onEvent("nameInput", "change", function() {
  username = getText("nameInput");
  updateScreen();
});

// Update the colour whenever the dropdown changes.
onEvent("colorDrop", "change", function() {
  color = getText("colorDrop");
  updateScreen();
});

// Increase the age.
onEvent("upBtn", "click", function() {
  age = age + 1;
  setText("ageTextArea", age);
  updateScreen();
});
// Decrease the age.
onEvent("downBtn", "click", function() {
  age = age - 1;
  setText("ageTextArea", age);
  updateScreen();
});

// This considers the input and updates the screen.
function updateScreen() {
  if (color == "red" && age > 16) {
    output = "rosy.";
  } else if (color == "red" && age <= 16) {
    output = "rad!.";
  }
  if (color == "blue" && age > 30) {
    output = "awful.";
  } else if (color == "blue" && age <= 30) {
    output = "brilliant.";
  }
  if (color != "blue" && color != "red" && age < 10) {
    output = "childish.";
  } else if (color != "blue" && color != "red") {
    output = "colorful.";
  }
  var myText = "Hello " + username;
  myText = myText + ", I see the future, your year is going to be" + output;
  setText("mainArea", myText);
}
