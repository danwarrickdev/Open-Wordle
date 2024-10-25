import sys
from game import Game


def game_loop():
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
            sys.exit()
        else:
            print("Invalid input")


def menu_loop():
    while True:
        Game.clear_screen()
        print(
            """ 
            +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+
            |O|p|e|n| |W|o|r|d|l|e| |v|1|.|0|
            +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+
            
            1 - Daily Game
            2 - View Stats
            3 - Quit
            """
        )
        i = input()
        match (i):
            case "1":
                game_loop()
            case "2":
                print_stats()
            case "3":
                Game.clear_screen()
                sys.exit()


def print_stats():
    print("hello")


def main():
    menu_loop()


if __name__ == "__main__":
    main()
