import random


def main():
    # Get word from array with random.choice
    answer = random.choice(["HELLO", "WORLD"])
    # Print board
    for _ in range(5):
        output_row(answer)

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


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
