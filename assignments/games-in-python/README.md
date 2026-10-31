
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game that practices Python strings, loops, conditionals, user input, and random selection. Players will reveal a hidden word by guessing its letters before they run out of attempts.

## 📝 Tasks

### 🛠️ Set Up and Display the Game

#### Description
Choose a secret word from the provided list, initialize the game state, and show the player's progress before each guess.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Track guessed letters and the number of incorrect guesses, using a maximum of 6 incorrect guesses.
- Display each letter that has been guessed correctly in its position and use underscores for unrevealed letters.
- Display the incorrect guesses remaining.


### 🛠️ Process Guesses and Finish the Game

#### Description
Prompt the player to guess letters, update the game state, and finish with the appropriate result when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Accept one letter per guess and treat uppercase and lowercase versions of the same letter equally.
- Reveal all matching positions for a correct guess.
- Reduce the remaining attempts for an incorrect guess; do not reduce attempts for a letter already guessed.
- End when the player reveals every letter in the secret word or uses all incorrect guesses.
- Display a win or loss message and reveal the secret word if the player loses.
