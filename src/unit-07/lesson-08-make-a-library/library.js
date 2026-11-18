// Unit 7, Lesson 8 — Project: Make a Library (Cereal Nutrition library)
// Reconstructed from the answer-key video:
//   "Code.org Project Lesson 8 Make a Library | Tutorial with Answers | Full App"
//   Mr. Kaiser — https://youtu.be/1joEzBtosrY
// Code is visible around 10:00 (top half) and 16:40 (bottom half).
//
// This is a LIBRARY, not an app: it exposes functions that another App Lab
// project can import. The data table "Cereal Nutrition" must be available to
// the library (import it in the project that uses the library).

// Return a random index that is valid for the cereal table.
function getRandomIndex() {
  var nameList = getColumn("Cereal Nutrition", "Name");
  var index = randomNumber(0, nameList.length - 1);
  return index;
}

// Return the cereal name at a given row.
function getName(index) {
  var nameList = getColumn("Cereal Nutrition", "Name");
  var name = nameList[index];
  return name;
}

// Return the box image for a given row.
function getCerealImage(index) {
  var allPictures = getColumn("Cereal Nutrition", "Box Image");
  var picture = allPictures[index];
  return picture;
}

// Check whether a calorie guess matches the cereal at this row.
function checkCalories(guess, index) {
  var correct = false;
  var allCalories = getColumn("Cereal Nutrition", "Calories");
  if (guess == allCalories[index]) {
    correct = true;
  }
  return correct;
}

// Count how many cereals have the guessed calorie value.
function allCaloriesCheck(guess) {
  var allCalories = getColumn("Cereal Nutrition", "Calories");
  var count = 0;
  for (var i = 0; i < allCalories.length; i++) {
    if (guess == allCalories[i]) {
      count = count + 1;
    }
  }
  return count;
}
