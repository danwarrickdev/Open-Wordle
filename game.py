from os import name, system
import random
import sys
from letter_box import LetterBox
from colorama import Style, Fore
import re

MAX_TRIES = 6
WORD_LENGTH = 5

class Game:
    def __init__(self) -> None:
        self._tries = MAX_TRIES
        self._guesses = []
        self._answer = random.choice(["hello", "world"])

        alphabet = "abcdefghijklmnopqrstuvwxyz"
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

    def check_win_loss_continue(self):
        last_guess = self._guesses[-1]
        if last_guess == self._answer:
            self.clear_screen()
            self.print_board()
            print("Success! :D")
            print(f"You solved it in {MAX_TRIES - self._tries + 1} tries!")
            sys.exit()
        elif self._tries == 0:
            print("Fail :(")
            print(f"The answer was {self._answer}")
            sys.exit()
        else:
            self.decrement_tries()
            self.clear_screen()

    def clear_screen(self):
        # windows clear terminal
        if name == "nt":
            system("cls")

        # mac/linux
        else:
            system("clear")

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