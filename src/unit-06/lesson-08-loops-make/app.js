// Unit 6, Lesson 8 — Loops Make: Lock Screen Maker app
// Reconstructed from the answer-key video:
//   "Code.org Lesson 8 Loops Lock Screen Maker App | Tutorial with Answers"
//   Mr. Kaiser — https://youtu.be/B-yYUaC5GxE
// Code is visible around 10:00 (events), 21:40 (changeColors) and 23:20 (changeShapes).
//
// App Lab text mode. Required design elements:
//   homeScreen                     screen
//   shapesButton                   button      ("Shapes!")
//   locationsButton                button      ("Locations!")
//   colorsButton                   button      ("Colors!")
//   icon0 … icon19                 20 images  (the lock-screen icons)

// List of icons to randomly choose between.
var iconIndex = -1;
var iconsList = [
  "icon://fa-heart",
  "icon://fa-music",
  "icon://fa-smile-o",
  "icon://fa-globe",
  "icon://fa-tree",
  "icon://fa-bolt",
  "icon://fa-moon-o",
  "icon://fa-star"
];

// Give the screen a random set of icons as soon as the app starts.
changeShapes();

onEvent("shapesButton", "click", function() {
  changeShapes();
});
onEvent("locationsButton", "click", function() {
  changeLocations();
});
onEvent("colorsButton", "click", function() {
  changeColors();
});

// Loop through all 20 icons and give each one a new random colour.
// The background reuses the last random values, tinted in a different order.
function changeColors() {
  for (var i = 0; i < 20; i++) {
    var red = randomNumber(0, 255);
    var green = randomNumber(0, 255);
    var blue = randomNumber(0, 255);
    setProperty("icon" + i, "icon-color", rgb(red, green, blue, 0.5));
  }
  setProperty("homeScreen", "background-color", rgb(green, blue, red, 0.5));
}

// Pick a different icon from the list, then apply it to every icon element.
function changeShapes() {
  var lastIndex = iconIndex;
  iconIndex = randomNumber(0, iconsList.length - 1);
  // Don't let the new shape be the same as the old one.
  while (iconIndex == lastIndex) {
    iconIndex = randomNumber(0, iconsList.length - 1);
  }
  // Loop through icons to assign images.
  for (var i = 0; i < 20; i++) {
    setProperty("icon" + i, "image", iconsList[iconIndex]);
  }
}

// Move every icon to a new random spot on the lock screen.
function changeLocations() {
  for (var i = 0; i < 20; i++) {
    setProperty("icon" + i, "x", randomNumber(50, 270));
    setProperty("icon" + i, "y", randomNumber(50, 400));
  }
}
