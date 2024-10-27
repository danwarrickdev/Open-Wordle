from os import name, system

def clear_screen():
    # windows clear terminal
    if name == "nt":
        system("cls")

    # mac/linux
    else:
        system("clear")