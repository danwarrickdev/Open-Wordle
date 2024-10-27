import json
import helpers
import sys

class Stats:
    def __init__(self) -> None:
        stats = self.get_stats()
        self._wins = stats["wins"]
        self._losses = stats["losses"]
        self._streak = stats["streak"]
        self._max_streak = stats["max_streak"]
        self._dist = stats["distribution"]
    
    @property
    def wins(self)->int:
        return self._wins

    @property
    def losses(self)->int:
        return self._losses

    @property
    def streak(self):
        return self._streak

    @property
    def max_streak(self):
        return self._max_streak
    
    @property
    def dist(self):
        return self._dist
    
    
    def get_stats(self):
        with open("data/stats.json") as file:
            d = json.load(file)
            return d
        
        
    def print_stats(self):
        helpers.clear_screen()
        
        total_plays = self.wins + self.losses
        win_percent = self.wins / total_plays * 100
        print(
            f""" 
+-+-+-+-+-+-+-+-+-+-+
|S|t|a|t|i|s|t|i|c|s
+-+-+-+-+-+-+-+-+-+-+

Played: {total_plays}
Win Percent: {win_percent:.1f}%
Current Win Streak: {self.streak}
Longest Win Streak: {self.max_streak}
            """
        )
        print(
            f""" 
+-+-+-+-+-+-+-+-+-+-+-+-+
|D|i|s|t|r|i|b|u|t|i|o|n
+-+-+-+-+-+-+-+-+-+-+-+-+
\nTotal Wins: {self.wins}
            """
        )
        dist = self.dist
        for i in dist:
            s = ""
            percent = dist[i] / self.wins * 100
            for j in range(round(percent)):
                if j % 10 == 0:
                    s += "🟩"
            s += f" {dist[i]} ({percent:.1f}%)"
            print(
                f"{i} : {s}",
            )
        while True:
            i = input("\nBack to menu (y/n)? ")
            if i.lower() == "y":
                break
            elif i.lower() == "n":
                helpers.clear_screen
                sys.exit()
            else:
                print("Invalid input")
