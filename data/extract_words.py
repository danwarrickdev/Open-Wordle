import re

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
            file.write(i + '\n')
            
if __name__ == "__main__":
    main()