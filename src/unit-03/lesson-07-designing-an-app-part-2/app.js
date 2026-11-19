// Unit 3, Lesson 7 — Project: Designing an App, Part 2
// "Coding Quiz" — the four-question quiz app built in the walkthrough.
// Reconstructed from the answer-key video:
//   "Code.org Lesson 7 Project Designing an App Part 2 | Answer Tutorial | Unit 3 CS Principles"
//   Mr. Kaiser — https://youtu.be/ItucouYL8y4
//
// App Lab text mode. Required screens:
//   homeScreen, q1Screen, q2Screen, q3Screen, q4Screen, winScreen, loseScreen
//
// Required buttons:
//   startBtn
//   q1CppBtn, q1PyBtn, q1JavaBtn, q1JSBtn
//   q2VBBtn, q2PyBtn, q2JavaBtn, q2JSBtn
//   q3VBBtn, q3CSharpBtn, q3JavaBtn, q3JSBtn
//   q4CppBtn, q4PyBtn, q4VBBtn, q4JSBtn
//   winPlayAgainBtn, losePlayAgain

// Start the quiz and play the startup sound.
onEvent("startBtn", "click", function() {
  setScreen("q1Screen");
  playSound("sound://category_digital/startup.mp3", false);
});

// Question 1: the correct answer is C++.
onEvent("q1CppBtn", "click", function() {
  setScreen("q2Screen");
});
// Wikimedia User:OgreBot/Uploads by new users
onEvent("q1PyBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q1JavaBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q1JSBtn", "click", function() {
  setScreen("loseScreen");
});

// Question 2: the correct answer is Python.
onEvent("q2VBBtn", "click", function() {
  setScreen("loseScreen");
});
// Wikimedia User:OgreBot/Uploads by new users
onEvent("q2PyBtn", "click", function() {
  setScreen("q3Screen");
});
onEvent("q2JavaBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q2JSBtn", "click", function() {
  setScreen("loseScreen");
});

// Question 3: the correct answer is Java.
onEvent("q3VBBtn", "click", function() {
  setScreen("loseScreen");
});
// https://commons.wikimedia.org/wiki/File:Nintendo-DSi-XL-Burgundy.png
onEvent("q3CSharpBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q3JavaBtn", "click", function() {
  setScreen("q4Screen");
});
onEvent("q3JSBtn", "click", function() {
  setScreen("loseScreen");
});

// Question 4: the correct answer is JavaScript.
onEvent("q4CppBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q4PyBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q4VBBtn", "click", function() {
  setScreen("loseScreen");
});
onEvent("q4JSBtn", "click", function() {
  setScreen("winScreen");
});

// Win / Lose screens: play a sound and go back to the start.
onEvent("winPlayAgainBtn", "click", function() {
  playSound("sound://category_digital/win.mp3", false);
  setScreen("homeScreen");
});
onEvent("losePlayAgain", "click", function() {
  playSound("sound://category_digital/failure.mp3", false);
  setScreen("homeScreen");
});
