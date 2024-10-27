import sys
from game import Game
import helpers
from stats import Stats

def game_loop():
    g = Game()
    helpers.clear_screen()

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

        if g.validate_is_word(i) == False:
            print("Word not found")
            continue

        # Check guess
        g.guess(i)

        # Update letter bank
        g.update_letter_bank()

        # Increment moves / Handle Win/Loss
        should_exit = g.check_win_loss_continue()
        if should_exit:
            break

        # Update board
        g.print_board()

        # Print letter bank
        g.print_letter_bank()

        print(f"{g.tries} tries remaining...")

    while True:
        i = input("Back to menu (y/n)? ")
        if i.lower() == "y":
            break
        elif i.lower() == "n":
            helpers.clear_screen()
            sys.exit()
        else:
            print("Invalid input")


def menu_loop():
    while True:
        helpers.clear_screen()
        helpers.print_header("Open Wordle v1.0")
        options = ["1 - New Puzzle", "2 - View Stats", "3 - Quit"]
        for o in options:
            print(o)
            
        i = input()
        match (i):
            case "1":
                game_loop()
            case "2":
                s = Stats()
                s.print_stats()
            case "3":
                helpers.clear_screen()
                sys.exit()


def main():
    menu_loop()


if __name__ == "__main__":
    main()
