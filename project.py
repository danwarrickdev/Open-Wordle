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
        i = input("Guess: ").lower()
        if i == "quit":
            sys.exit()

        # Validate user input
        if g.validate_guess(i) == False:
            print("Invalid Input")
            continue
        
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


if __name__ == "__main__":
    main()
