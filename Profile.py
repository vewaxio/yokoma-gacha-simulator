from Menu import Menu, printMenu, printTitle
from MenuItem import MenuItem

class Profile:
    def __init__(self, name = None,  yokoyen = None, gacha = None, inventory = None, achievement = None, difficulty = "", combination_count = None, accumulated_yokoyen = None):
        self.name = name
        self.yokoyen = yokoyen
        self.gacha = gacha
        self.inventory = inventory
        self.achievement = achievement
        self.difficulty = difficulty
        self.combination_count = combination_count or 0
        self.accumulated_yokoyen = accumulated_yokoyen or 0

    def printProfile(self):
        printTitle("title", f"{self.name.upper()}'S PROFILE", 40, 0)
        printMenu(MenuItem("Difficulty", self.difficulty))
        printMenu(MenuItem("Yokoyen Possessed", f"{self.yokoyen:,}"))
        printMenu(MenuItem("Amount of Times Pulled", f"{self.gacha.pull_count:,}"))
        printMenu(MenuItem("Achievements Completed", self.achievement.checkCompleted()))
        printMenu(MenuItem("Total Combinations Done", f"{self.combination_count:,}"))
        printMenu(MenuItem("Total Earning", f"{self.accumulated_yokoyen:,}"))
        printTitle("close", None, 40, 0)