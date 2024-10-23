import sys
from game import Game


def main():
    g = Game()
    g.clear_screen()

    # Print board
    g.print_board()

    # Print letter bank
    g.print_letter_bank()

    # Get user input
    while True:
        # Get guess
        i = input("Guess:").lower()
        if i == "quit":
            sys.exit()

        # Validate user input
        # Check guess
        g.guess(i)

        # Update letter bank
        g.update_letter_bank()

        # Increment moves / Handle Win/Loss
        g.check_win_loss_continue()

        # Update board
        g.print_board()

        # Print letter bank
        g.print_letter_bank()

        print(f"{g.tries} tries remaining...")





def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
