import random
from colorama import Style
import sys
from os import name, system


def main():
    clear_screen()
    # Get word from array with random.choice
    answer = random.choice(["hello", "world"])
    tries = 5
    guesses = []

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
        guesses.append(i)

        # Increment moves / Handle Win/Loss
        if i == answer:
            print("Success! :D")
            sys.exit()
        elif tries == 0:
            print("Fail :(")
            print(f"The answer was {answer}")
            sys.exit()
        else:
            tries -= 1
            clear_screen()

        # Update board
        for num in range(5):
            if num < len(guesses):
                output_guess_row(guesses[num], answer)
            else:
                output_empty_row()

        for letter in i:
            letter_bank[letter]["is_guessed"] = True
        output_letter_bank(letter_bank)
        print(f"{tries} tries remaining...")

    # Update letter bank
    # On Win -> update stats, congrat message
    # On Lose -> update stats, loss message


def output_guess_row(guess, answer):
    output = [
        "",
        "",
        "",
    ]

    index = 0
    for letter in guess:
        color = "white"
        if letter in answer:
            color = "yellow"
            if guess[index] == answer[index]:
                color = "green"
        box = get_letter_box(letter, color)
        for i in range(3):
            output[i] += box[i]
        index += 1

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
        box = get_letter_box("?")
        for i in range(3):
            output[i] += box[i]

    for i in output:
        print(i)
    print()


def get_letter_box(s, color="white"):
    if color == "green":
        return ["🟩🟩🟩 ", f"🟩{s.capitalize()} 🟩 ", "🟩🟩🟩 "]
    elif color == "yellow":
        return ["🟨🟨🟨 ", f"🟨{s.capitalize()} 🟨 ", "🟨🟨🟨 "]
    else:
        return ["⬜⬜⬜ ", f"⬜{s.capitalize()} ⬜ ", "⬜⬜⬜ "]


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


def clear_screen():
    # windows clear terminal
    if name == "nt":
        system("cls")

    # mac/linux
    else:
        system("clear")


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
