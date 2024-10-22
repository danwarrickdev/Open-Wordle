import random
from colorama import Fore, Back, Style


def main():
    # Get word from array with random.choice
    answer = random.choice(["HELLO", "WORLD"])
    # Print board
    for _ in range(5):
        output_row(answer)

    letter_bank = init_letter_bank()

    index = 0
    for i in letter_bank:
        if letter_bank[i]["is_guessed"]:
            print(Style.DIM + i.capitalize() + "\u0336", end="  ")
        else:
            print(i.capitalize(), end="  ")
        if (index + 1) % 10 == 0:
            print()
        index += 1

    # Print letter bank
    # Get user input
    # Validate user input
    # Check guess
    # Increment moves / Handle Win/Loss
    # Update board
    # Update letter bank
    # On Win -> update stats, congrat message
    # On Lose -> update stats, loss message


def output_row(word="?????"):
    output = [
        "",
        "",
        "",
    ]

    for letter in word:
        box = get_letter_box(letter)
        for i in range(3):
            output[i] += box[i]

    for i in output:
        print(i)
    print()


def get_letter_box(s, color="white"):
    if color == "green":
        return ["🟩🟩🟩 ", f"🟩{s} 🟩 ", "🟩🟩🟩 "]
    elif color == "yellow":
        return ["🟨🟨🟨 ", f"🟨{s} 🟨 ", "🟨🟨🟨 "]
    else:
        return ["⬜⬜⬜ ", f"⬜{s} ⬜ ", "⬜⬜⬜ "]


def init_letter_bank():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return {
        letter: {"is_guessed": False, "is_correct": False, "is_hint": False}
        for letter in alphabet
    }


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
