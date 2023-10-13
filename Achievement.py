from colorama import init, Fore, Back, Style
from Menu import Menu, printMenu, printTitle
from MenuItem import MenuItem

class Achievement:
    def __init__(self):
        self.achievements = []

        # Generate achievements
        self.addAchievement(1, "Gacha Enthusiast", "Pull Yokoma at least 100 times", 100)
        self.addAchievement(2, "Gacha Master", "Pull Yokoma at least 500 times", 500)
        self.addAchievement(3, "Gacha Legend", "Pull Yokoma at least 1,000 times", 1000)
        self.addAchievement(4, "Gacha Guru", "Pull Yokoma at least 5,000 times", 5000)
        self.addAchievement(5, "Gacha God", "Pull Yokoma at least 10,000 times", 10000)
        self.addAchievement(6, "Wealthy Collector", "Earn a total of 10,000 Yokoyen", 10000)
        self.addAchievement(7, "Master Collector", "Earn a total of 50,000 Yokoyen", 50000)
        self.addAchievement(8, "Legend Collector", "Earn a total of 100,000 Yokoyen", 100000)
        self.addAchievement(9, "Guru Collector", "Earn a total of 500,000 Yokoyen", 500000)
        self.addAchievement(10, "God Collector", "Earn a total of 1,000,000 Yokoyen", 1000000)
        self.addAchievement(11, "Master Combiner", "Combine Yokoma at least 50 times", 50)
        self.addAchievement(12, "Legend Combiner", "Combine Yokoma at least 100 times", 100)
        self.addAchievement(13, "Guru Combiner", "Combine Yokoma at least 500 times", 500)
        self.addAchievement(14, "God Combiner", "Combine Yokoma at least 1,000 times", 1000)


    def addAchievement(self, id, name, description, goal, progress = 0, completed = False):
        achievement= {
            "ID": id,
            "name": name,
            "description": description,
            "goal": goal,
            "progress": progress or 0,
            "completed": completed,
            "status": "Completed" if completed else "Not Completed"
        }
        self.achievements.append(achievement)

    def updateProgress(self):
        for achievement in self.achievements:
            # bug handling
            if achievement["progress"] < achievement["goal"]:
                achievement["Completed"] = False
                achievement["status"] = "Completed" if achievement["completed"] else "Not Completed"

            # check achievement
            if (achievement["completed"]):
                continue
            if achievement["progress"] >= achievement["goal"]:
                achievement["completed"] = True
                achievement["status"] = "Completed" if achievement["completed"] else "Not Completed"
                title = (f"You have completed {achievement['name']}!")
                printTitle('title', title)
    
    def listAchievements(self):
        printTitle('title', f"ACHIEVEMENTS ({self.checkCompleted()}/{len(self.achievements)})", 80, 0)
        for index, achievement in enumerate(self.achievements):
            color = Fore.GREEN if achievement["completed"] else Fore.RED
            printMenu(MenuItem(f"{index + 1}", color + f"{achievement['name']}: {achievement['status']} - Progress: {achievement['progress']:,}/{achievement['goal']:,}"))
            printMenu(MenuItem(Fore.LIGHTBLACK_EX + 'Detail', achievement['description']))
        printTitle('close', None, 80, 0)
    
    def checkCompleted(self):
        self.achievement_count = 0
        for achievement in self.achievements:
            if achievement["completed"]:
                self.achievement_count += 1
        return self.achievement_count


