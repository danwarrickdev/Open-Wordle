import helpers

PATH_TO_STATS = "data/stats.json"

class Stats:
    def __init__(self) -> None:
        stats: dict = self.get_stats()
        self._wins: int = stats["wins"]
        self._losses: int = stats["losses"]
        self._streak: int = stats["streak"]
        self._max_streak: int = stats["max_streak"]
        self._dist: dict = stats["distribution"]
    
    @property
    def wins(self) -> int:
        return self._wins

    @property
    def losses(self) -> int:
        return self._losses

    @property
    def streak(self) -> int:
        return self._streak

    @property
    def max_streak(self):
        return self._max_streak
    
    @property
    def dist(self) -> dict:
        return self._dist
        
        
    def print_stats(self) -> None:
        helpers.clear_screen()
        
        total_plays = self.wins + self.losses
        win_percent = self.wins / total_plays * 100
        
        helpers.print_header("Statistics")
        basic_stats = [
            f"Played: {total_plays}", 
            f"Wins: {self.wins}",
            f"Win Percent: {win_percent:.1f}%", 
            f"Current Win Streak: {self.streak}", 
            f"Longest Win Streak: {self.max_streak}\n",
        ]
        for b in basic_stats:
            print(b)
        
        helpers.print_header("Distribution")
        
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
        helpers.back_to_menu_loop()

    @classmethod
    def get_stats(cls) -> dict:
        return helpers.read_json(PATH_TO_STATS)
    
    @classmethod
    def update_stats(cls, win: int, tries: int) -> None:
        stats = cls.get_stats()

        if win:
            stats["wins"] += 1
            stats["streak"] += 1
        else:
            stats["losses"] += 1
            stats["streak"] = 0

        if stats["streak"] > stats["max_streak"]:
            stats["max_streak"] += 1

        distribution = stats["distribution"]
        distribution[str(tries)] += 1
        stats["distribution"] = distribution
        
        helpers.write_json(PATH_TO_STATS, stats)