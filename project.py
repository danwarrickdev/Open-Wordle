import random
from colorama import Style
import sys
from os import name, system
from letter_box import LetterBox
from game import Game


def main():
    g = Game()
    g.clear_screen()

    # Print board
    for _ in range(5):
        output_empty_row()

    # Print letter bank
    letter_bank = init_letter_bank()
    output_letter_bank(letter_bank)

    # Get user input
    while True:
        # Get guess
        i = input("Guess:").lower()
        if i == "quit":
            sys.exit()

        # Validate user input
        # Check guess
        g.guess(i)

        # Increment moves / Handle Win/Loss
        g.check_win_loss_continue()

        # Update board
        for num in range(5):
            if num < len(g.guesses):
                output_guess_row(g.guesses[num], g.answer)
            else:
                output_empty_row()

        for letter in i:
            letter_bank[letter]["is_guessed"] = True
        output_letter_bank(letter_bank)
        print(f"{g.tries} tries remaining...")

    # Update letter bank
    # On Win -> update stats, congrat message
    # On Lose -> update stats, loss message


def output_guess_row(guess, answer):
    output = [
        "",
        "",
        "",
    ]

    letter_boxes = [LetterBox(i, guess[i]) for i in range(len(guess))]
    print(letter_boxes)
    for b in letter_boxes:
        color = b.get_color(guess, answer)
        box = b.__str__(color)

        for i in range(3):
            output[i] += box[i]

    for i in output:
        print(i)
    print()


def output_empty_row():
    output = [
        "",
        "",
        "",
    ]

    for _ in range(5):
        b = LetterBox(-1, "?")
        box = b.__str__("white")

        for i in range(3):
            output[i] += box[i]

    for i in output:
        print(i)
    print()


def init_letter_bank():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return {
        letter: {"is_guessed": False, "is_correct": False, "is_hint": False}
        for letter in alphabet
    }


def output_letter_bank(letter_bank):
    index = 0
    for i in letter_bank:
        if letter_bank[i]["is_guessed"]:
            print(Style.DIM + i.capitalize() + "\u0336", end="  ")
        else:
            print(Style.RESET_ALL + i.capitalize(), end="  ")
        if (index + 1) % 10 == 0:
            print()
        index += 1
    print()


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
