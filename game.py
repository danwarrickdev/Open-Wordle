from os import name, system
import random
import sys


class Game:
    def __init__(self) -> None:
        self._tries = 5
        self._guesses = []
        self._answer = random.choice(["hello", "world"])

    @property
    def tries(self):
        return self._tries

    @property
    def guesses(self):
        return self._guesses

    @property
    def answer(self):
        return self._answer

    def decrement_tries(self):
        self._tries -= 1

    def guess(self, g):
        self._guesses.append(g)

    def check_win_loss_continue(self):
        last_guess = self._guesses[-1]
        if last_guess == self._answer:
            print("Success! :D")
            sys.exit()
        elif self._tries == 0:
            print("Fail :(")
            print(f"The answer was {self._answer}")
            sys.exit()
        else:
            self.decrement_tries()
            self.clear_screen()

    @classmethod
    def clear_screen(self):
        # windows clear terminal
        if name == "nt":
            system("cls")

        # mac/linux
        else:
            system("clear")
