import re
import json


def main():
    raw = read_file()
    validated = []
    for i in raw:
        if re.search(r"^[a-z]{5}", i) and len(i) == 5:
            validated.append(i)
    write_file(validated)


def read_file():
    arr = []
    with open("raw.txt", "r") as file:
        for line in file:
            arr.append(line.strip())
    return arr


def write_file(arr):
    with open("dictionary.txt", "a") as file:
        for i in arr:
            file.write(i + "\n")


def generate_word_json():
    word_bank = {}
    with open("word_bank.txt", "r") as file:
        for line in file:
            word = line.strip()
            word_bank[word] = {"is_used": False}

    with open("words.json", "w", encoding="utf-8") as f:
        json.dump(word_bank, f, indent=4)


if __name__ == "__main__":
    # main()
    generate_word_json()
