from os import name, system
import json
import sys

def clear_screen() -> None:
    # windows clear terminal
    if name == "nt":
        system("cls")

    # mac/linux
    else:
        system("clear")

def read_json(filename: str) -> dict:
    with open(filename) as file:
        d = json.load(file)
        file.close()
        return d

def write_json(filename: str, values: dict) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(values, file, indent=4)
        file.close()

def read_txt(filename: str) -> list[str]:
    arr = []
    with open(filename, "r") as file:
        for line in file:
            arr.append(line.strip().lower())
    return arr

"""
            +-+-+-+-+-+-+
header ->   |H|e|a|d|e|r|
            +-+-+-+-+-+-+
"""
def print_header(s: str) -> None:
    words = s.split(" ")
    output = ""
    top, mid, bottom = "","",""
    for word in words:
        for l in word:
            top += "+-"
            mid += f"|{l}"
            bottom += "+-"
        top += "+ "
        mid += "| "
        bottom += "+ "
    output += f"{top}\n{mid}\n{bottom}\n"
    print(output)
            
def back_to_menu_loop() -> None:
    while True:
        i = input("\nBack to menu (y/n)? ")
        if i.lower() == "y":
            break
        elif i.lower() == "n":
            clear_screen()
            sys.exit()
        else:
            print("Invalid input")