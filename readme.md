# Open Wordle

#### Video Demo:

https://youtu.be/bGnoGbZcbKM

#### Description:

This project is a recreation of the game "Wordle", currently owned by the New York Times.  It can be run ad-free in your terminal with Python 3 and includes 1500+ puzzles without the 1-puzzle-per-day limit.  Open Wordle also supports functionality for displaying your play statistics (wins, losses, distribution, etc.) and will save these stats locally.

#### How to Play:

Wordle is at its core a "guess the word" game.  All answers are 5 letters and you have 6 attempts to guess the correct word.  When you make a guess, if any of the letters are included in the answer, they will be displayed with a highlight color.  Yellow means the letter exists in the answer but is in the wrong position.  Green means the letter is in the correct position.  Your guess must be an actual english word.  Making a guess that is not a word will not count against your attempts and should prompt you to try again.  The game ends when you correctly guess the word (all letters are green) or you run out of attempts.

#### Setup Instructions:

```
# clone repo with ssh
git clone git@github.com:danwarrickdev/Open-Wordle.git

# change directory
cd open-wordle

# install dependencies
pip install -r requirements.txt

# run game
python project.py
```

#### Data

Open Wordle (OW) currently includes a word bank of 1545 possible answers.  This list was generated through several steps.  I began with the english-words project (https://github.com/dwyl/english-words ) on github which contains 400k+ words.  I then used a python script to filter out all non-five-letter words.  Finally, I manually stepped through this filtered list and curated a smaller subset of words the average english speaker is likely to know.  OW contains a /data directory which includes the methods used to generate this word bank.

#### Classes

#### Game

***Description*:**

This class contains the top-level functions and variables necessary for executing the main game loop.

***Variables***

`Game._tries : int`

Number of times to execute the main game loop

`Game._guesses : str[]`

Player guesses for display purposes

`Game._answer : str`

The word the user is trying to guess

`Game._all_words : str[]`

A list of 400k words to validate guesses are actual words

`Game._letter_bank : Dictionary`

Used to display letters guessed

***Functions***

`Game.decrement_tries() -> None`

Decrements tries by 1

`Game.guess(g: str) -> None`

Appends a string to the guesses array

`Game.check_win_loss_continue() -> bool`

Checks if the most recent guess is equal to the answer.  If correct or user is out of tries, returns True (should_exit). Else, returns False.

`Game.print_row(g?: str) -> None`

Outputs a row of LetterBoxes with the appropriate colors.

`Game.print_board() -> None`

Invokes `print_row` multiple times to output the game board

`Game.update_letter_bank() -> None`

Updates letter_bank which determines whether a letter in the bank should be displayed as plain, strikethrough, or with a color.

`Game.print_letter_bank() -> None`

Prints the letter bank with the appropriate styling

`Game.validate_guess(g: string) -> bool`

Returns true/false depending on if the guess passes a regex

`Game.validate_is_word(g: string) -> bool`

Returns true if a guess exists in all_words, else returns false

`Game.get_answer() -> str`

Reads word_bank.json, filters out previously guessed words, randomly selects a word from the bank to return and updates the word_bank.json to reflect that the selected word has been selected.

`Game.get_all_possible_words() -> str[]`

Reads raw.txt which contains 400k words and parses the file into an array of string.

#### LetterBox

***Description*:**

This class handles the individual boxes that make up the game board.  Each instance reflects an individual box/letter in the answer.

***Variables***

`LetterBox._index : int`

Index of the letter's position in the answer

`LetterBox._value : str`

String value of the character in the answer

***Functions***

`LetterBox.get(c ?: str) -> str[]`

Returns a string array with 3 elements, to be used to display the letter box on the board

`LetterBox.get_color(guess: str, answer: str) -> "white" | "yellow" | "green"`

Returns the color the LetterBox should be displayed as on the game board

`LetterBox.find_all(s: string, char: str) -> int[]`

Searches a string for all instances of a character and returns an array containing all indexes where these chars appear 

#### Stats

***Description***
This class is used to display and save the players gameplay statistics.

***Variables***

`Stats._wins : int`

Number of times a player has solved a puzzle

`Stats._losses : int`

Number of times a player has failed to solve the puzzle

`Stats._streak : int`

Current number of consecutive wins

`Stats._max_streak : int`

Longest running number of consecutive wins

`Stats._distribution : Dictionary`

Dictionary containing a count for how many times the player has solved the puzzle in x number of attempts

***Functions***

`Stats.get_stats() -> JSON`

Reads stats.json and returns a dictionary containing the files contents

`Stats.print_stats() -> None`

Prints users gameplay statistics and graphically represents the distribution of their wins as a horizontal bar chart.

`Stats.update_stats(win: bool, tries: int)`

Updates stats.json after a puzzle is succeeded/failed