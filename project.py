import sys
from game import Game
import helpers
from stats import Stats
from letter_box import LetterBox

def game_loop() -> None:
    g = Game()
    helpers.clear_screen()

    # Print board
    g.print_board()

    # Print letter bank
    g.print_letter_bank()

    # Get user input
    while True:

        # Get guess
        i = input("\nGuess: ").lower()
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

    helpers.back_to_menu_loop()

# Main Menu - Get user input and route to either game/stats/quit
def menu_loop() -> None:
    while True:
        helpers.clear_screen()
        helpers.print_header("Open Wordle v1.0")
        options = ["1 - New Puzzle", "2 - View Stats", "3 - Quit"]
        for o in options:
            print(o)
            
        i = input("\n")
        match (i):
            case "1":
                game_loop()
            case "2":
                s = Stats()
                s.print_stats()
            case "3":
                helpers.clear_screen()
                sys.exit()


def get_letterbox_str(index: int, value: str, color: str) -> list[str]:
    l = LetterBox(index,value)
    return l.get(color)

def get_letterbox_color(index: int, value: str, guess: str, answer: str) -> str:
    l = LetterBox(index, value)
    return l.get_color(guess, answer)

def find_all_chars_in_str(s: str, char: str) -> list[int]:
    return LetterBox.find_all(s, char)
    
def main() -> None:
    menu_loop()


if __name__ == "__main__":
    main()
