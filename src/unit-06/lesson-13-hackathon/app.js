// Unit 6, Lesson 13 — Project: Hackathon
// Example hackathon app: "AP CS Test Taker Demographics".
// Reconstructed from the complete-project walkthrough:
//   "Code.org Hackathon App - Complete Project Tutorial - All Parts | Unit 6 CSP"
//   Mr. Kaiser — https://youtu.be/ChYHvfktgCE
//
// This is ONE example topic for the hackathon. The lesson asks you to choose your
// own topic and dataset; use this as a model for the pattern, not as your project.
//
// App Lab text mode. Required design elements:
//   homeScreen            screen with the title and the Race / Gender buttons
//   genderScreen          screen with the gender dropdown and output
//   raceScene             screen with the race dropdown and output
//   genderBtn             button on homeScreen
//   raceBtn               button on homeScreen
//   genderStatesDropDown  dropdown on genderScreen
//   raceStateDrop         dropdown on raceScene
//   genderOutput          label or text area on genderScreen
//   raceOutput            label or text area on raceScene
//   genderHomeBtn         button on genderScreen
//   raceHomeBtn           button on raceScene
//
// Import the "AP Computer Science Test Taker Demographics by State (2019)" table
// into the project's Data tab before running the app.

// Pull the columns we need out of the data table. Each getColumn call returns a list
// in the same row order, so index i in every list refers to the same state.
var states = getColumn("AP Computer Science Test Taker Demographics by State (2019)", "State");
var genderList = getColumn("AP Computer Science Test Taker Demographics by State (2019)", "Total % female");
var blackTestTakers = getColumn("AP Computer Science Test Taker Demographics by State (2019)", "Total Black");
var hispanicTestTakers = getColumn("AP Computer Science Test Taker Demographics by State (2019)", "Total Hispanic/Latino");
var americanTestTakers = getColumn("AP Computer Science Test Taker Demographics by State (2019)", "Total American Indian/Alaska Native");
var pacificTestTakers = getColumn("AP Computer Science Test Taker Demographics by State (2019)", "Total Native Hawaiian/Other Pacific Islander");

// The state currently chosen in whichever dropdown was last used.
var stateSelection = "Alabama";

// Home screen navigation.
onEvent("genderBtn", "click", function() {
  setScreen("genderScreen");
});

onEvent("raceBtn", "click", function() {
  setScreen("raceScene");
});

// Gender screen: find the row for the selected state, then show that row's percentage.
onEvent("genderStatesDropDown", "change", function() {
  stateSelection = getText("genderStatesDropDown");
  for (var i = 0; i < states.length; i++) {
    if (stateSelection == states[i]) {
      setText("genderOutput", genderList[i] + "% of test takers were female");
    }
  }
});

// Race screen: find the row for the selected state, then build a multi-line summary.
onEvent("raceStateDrop", "change", function() {
  stateSelection = getText("raceStateDrop");
  for (var i = 0; i < states.length; i++) {
    if (stateSelection == states[i]) {
      var output = "Students who took the exam.\n";
      output = output + "Black students: " + blackTestTakers[i];
      output = output + "\nHispanic/Latinos: " + hispanicTestTakers[i];
      output = output + "\nAmerican Indian: " + americanTestTakers[i];
      output = output + "\nPacific Islanders: " + pacificTestTakers[i];
      setText("raceOutput", output);
    }
  }
});

// Back to the home screen from either detail screen.
onEvent("genderHomeBtn", "click", function() {
  setScreen("homeScreen");
});

onEvent("raceHomeBtn", "click", function() {
  setScreen("homeScreen");
});
