// Unit 6, Lesson 12 — Traversals Make: Random Forecaster app
// Reconstructed from the answer-key video:
//   "Code.org Lesson 12 Traversals Make a Random Forecaster App | Answer Tutorial"
//   Mr. Kaiser — https://youtu.be/pk32rysRQAg
// Code is visible around 12:00 (filter loop) and 15:30 (updateScreen).
//
// App Lab text mode. Required design elements:
//   forecastButton     button   ("Get Forecast")
//   cityOutput         label
//   highTempOutput     label
//   lowTempOutput      label
//   conditionOutput    label
//   iconOutput         image
//
// The project must have the "Daily Weather" data table imported.

// Pull each column out of the table once.
var cities = getColumn("Daily Weather", "City");
var highs = getColumn("Daily Weather", "High Temperature");
var lows = getColumn("Daily Weather", "Low Temperature");
var conditions = getColumn("Daily Weather", "Main Condition");
var icons = getColumn("Daily Weather", "Icon");
var forecastNumbers = getColumn("Daily Weather", "Forecast Number");

// Filtered list: only the rows for tomorrow (Forecast Number 1).
var tomorrowCities = [];
var tomorrowHighs = [];
var tomorrowLows = [];
var tomorrowConditions = [];
var tomorrowIcons = [];

// Traverse the table and copy tomorrow's rows into the parallel lists.
for (var i = 0; i < cities.length; i++) {
  if (forecastNumbers[i] == 1) {
    appendItem(tomorrowCities, cities[i]);
    appendItem(tomorrowHighs, highs[i]);
    appendItem(tomorrowLows, lows[i]);
    appendItem(tomorrowConditions, conditions[i]);
    appendItem(tomorrowIcons, icons[i]);
  }
}

// Pick one random city from the filtered list and display all of its values.
function updateScreen() {
  var index = randomNumber(0, tomorrowCities.length - 1);

  setText("cityOutput", tomorrowCities[index]);
  setText("highTempOutput", tomorrowHighs[index]);
  setText("lowTempOutput", tomorrowLows[index]);
  setText("conditionOutput", tomorrowConditions[index]);
  setProperty("iconOutput", "image", tomorrowIcons[index]);
}

onEvent("forecastButton", "click", function() {
  updateScreen();
});
