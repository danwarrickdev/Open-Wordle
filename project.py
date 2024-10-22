import random


def main():
    # Get word from array with random.choice
    answer = random.choice(["hello", "world"])
    # Print board
    output_row(answer)
    output_row(answer)
    output_row(answer)
    output_row(answer)
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


def output_row(w="?????"):
    row_0 = ""
    row_1 = ""
    row_2 = ""
    row_3 = ""
    row_4 = ""
    for l in w:
        box = get_letter_box(l)
        row_0 += box[0]
        row_1 += box[1]
        row_2 += box[2]
        row_3 += box[3]
        row_4 += box[4]
    print(row_0)
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)


def get_letter_box(s):
    return [
        " ***** ",
        "|     |",
        f"|  {s}  |",
        "|     |",
        " ***** ",
    ]


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
