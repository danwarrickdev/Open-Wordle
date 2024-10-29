class LetterBox:
    # index, value, is_guessed, print
    def __init__(self, index, value) -> None:
        self._index: int = index
        self._value: str = value

    def get(self, color="white") -> list[str]:
        if color == "green":
            return ["🟩🟩🟩 ", f"🟩{self._value.capitalize()} 🟩 ", "🟩🟩🟩 "]
        elif color == "yellow":
            return ["🟨🟨🟨 ", f"🟨{self._value.capitalize()} 🟨 ", "🟨🟨🟨 "]
        else:
            return ["⬜⬜⬜ ", f"⬜{self._value.capitalize()} ⬜ ", "⬜⬜⬜ "]

    def get_color(self, guess: str, answer: str) -> str:
        color = "white"
            
        # does letter exist in answer
        if self._value in answer:
            color = "yellow"
            
            # is letter position same as in answer
            if guess[self._index] == answer[self._index]:
                color = "green"
            else:
                # get all instances of letter
                num_instance = self.find_all(answer, self._value)
                
                remaining_duplicate = False
                for i in num_instance:
                    # check if instances are green
                    if guess[i] != answer[i]:
                        remaining_duplicate = True
                # takes care of dupes
                if not remaining_duplicate:
                    color = "white"
        
        return color

    # get all indexes of a char in a string
    @classmethod
    def find_all(cls, s: str, char: str) -> list[int]:
        indexes = []
        index = -1
        while True:
            index = s.find(char, index+1)
            if index == -1:
                break
            else:
                indexes.append(index)
        return indexes