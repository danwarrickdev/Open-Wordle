import random
from letter_box import LetterBox
from colorama import Style, Fore
import re
import helpers
from stats import Stats

MAX_TRIES = 6
WORD_LENGTH = 5
PATH_TO_WORD_BANK = "data/words.json"
PATH_TO_RAW_WORD_LIST = "data/raw.txt"

class Game:
    def __init__(self) -> None:
        # number of times to execute game loop
        self._tries = MAX_TRIES
        
        # past guesses for display purposes
        self._guesses = []
        
        # the word the user is trying to guess
        self._answer = self.get_answer()
        
        # a list of 400k words to validate guesses are actual words
        self._all_words = self.get_all_possible_words()

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        # used to display letters guessed
        self._letter_bank = {
            letter: {"is_guessed": False, "is_correct": False, "is_hint": False}
            for letter in alphabet
        }

    @property
    def tries(self):
        return self._tries

    @property
    def guesses(self):
        return self._guesses

    @property
    def answer(self):
        return self._answer

    @property
    def letter_bank(self):
        return self._letter_bank

    def decrement_tries(self):
        self._tries -= 1

    def guess(self, g):
        self._guesses.append(g)

    # returns should_exit
    def check_win_loss_continue(self):
        last_guess = self._guesses[-1]
        tries = MAX_TRIES - self._tries + 1
        
        if last_guess == self._answer:
            helpers.clear_screen()
            self.print_board()
            print("Success! :D")
            print(f"You solved it in {tries} tries!")
            Stats.update_stats(True, tries)
            return True
        elif self._tries == 1:
            self.print_board()
            print("Fail :(")
            print(f"The answer was {self._answer}")
            Stats.update_stats(False, tries)
            return True
        else:
            self.decrement_tries()
            helpers.clear_screen()
            return False


    def print_row(self, guess=""):
        output = ["" for _ in range(3)]
        if guess and self._answer:
            # get guess string as list of LetterBox
            letter_boxes = [LetterBox(i, guess[i]) for i in range(WORD_LENGTH)]

            for b in letter_boxes:
                # Get output in correct color
                color = b.get_color(guess, self._answer)
                box = b.__str__(color)

                for i in range(3):
                    output[i] += box[i]
        else:
            # handle empty row
            for _ in range(WORD_LENGTH):
                b = LetterBox(-1, "?")
                box = b.__str__("white")

                for i in range(3):
                    output[i] += box[i]

        # print output
        for i in output:
            print(i)
        print()

    def print_board(self):
        # Update board
        for num in range(MAX_TRIES):
            if num < len(self._guesses):
                self.print_row(self._guesses[num])
            else:
                self.print_row()

    def update_letter_bank(self):
        last_guess = self._guesses[-1]
        index = 0
        for l in last_guess:
            self._letter_bank[l]["is_guessed"] = True
            if l in self._answer:
                self._letter_bank[l]["is_hint"] = True
                if last_guess[index] == self._answer[index]:
                    self._letter_bank[l]["is_correct"] = True
            index += 1

    def print_letter_bank(self):
        index = 0
        for i in self._letter_bank:
            if self._letter_bank[i]["is_correct"]:
                print(Style.RESET_ALL + Fore.GREEN + i.capitalize(), end="  ")
            elif self._letter_bank[i]["is_hint"]:
                print(Style.RESET_ALL + Fore.YELLOW + i.capitalize(), end="  ")
            elif self._letter_bank[i]["is_guessed"]:
                print(Style.RESET_ALL + Style.DIM + i.capitalize() + "\u0336", end="  ")
            else:
                print(Style.RESET_ALL + i.capitalize(), end="  ")
            if (index + 1) % 10 == 0:
                print()
            index += 1
        print()

    def validate_guess(self, guess):
        g = guess.strip().lower()
        try:
            if re.search(r"^[a-zA-Z]{5}", g):
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_is_word(self, guess):
        g = guess.strip().lower()

        return g in self._all_words

    def get_answer(self):
        words = helpers.read_json(PATH_TO_WORD_BANK)
        
        filtered = []
        
        # Get list of words that haven't been answers yet
        for word in words:
            if not words[word]["is_used"]:
                filtered.append(word)
        
        answer = ""
        new_words = {}
        
        if len(filtered)>0:
            new_words = {**words}
        else:
            # user has gone through whole db; reset
            new_words = {**words}
            for word in words:
                new_words[word] = {{"is_used": False}}
                filtered.append(word)
                
        answer = random.choice(filtered)
        new_words[answer] = {"is_used": True}

        helpers.write_json(PATH_TO_WORD_BANK, new_words)
        
        return answer

    def get_all_possible_words(self):
        return helpers.read_txt(PATH_TO_RAW_WORD_LIST)

        
    