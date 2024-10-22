class LetterBox:
    # index, value, is_guessed, print
    def __init__(self, index, value) -> None:
        self._index = index
        self._value = value

    def __str__(self, color="white"):
        if color == "green":
            return ["🟩🟩🟩 ", f"🟩{self._value.capitalize()} 🟩 ", "🟩🟩🟩 "]
        elif color == "yellow":
            return ["🟨🟨🟨 ", f"🟨{self._value.capitalize()} 🟨 ", "🟨🟨🟨 "]
        else:
            return ["⬜⬜⬜ ", f"⬜{self._value.capitalize()} ⬜ ", "⬜⬜⬜ "]

    def get_color(self, guess, answer):
        color = "white"
        if self._value in answer:
            color = "yellow"
            if guess[self._index] == answer[self._index]:
                color = "green"
        return color
