from Menu import Menu, printMenu, printTitle
from MenuItem import MenuItem
from colorama import init, Fore, Style

# CONST
# Define a color for each rarity
RARITY_COLORS = {
    'Pathetic': Fore.BLACK,
    'Trash': Fore.LIGHTBLACK_EX,
    'Common': Fore.WHITE,
    'Uncommon': Fore.YELLOW,
    'Rare': Fore.GREEN,
    'Unique': Fore.BLUE,
    'Legendary': Fore.MAGENTA,
    'Mythical': Fore.RED,
}

class Inventory:
    def __init__(self):
        self.yokoma_list = []
    
    def addYokoma(self, yokoma):
        self.yokoma_list.append(yokoma)
        self.printNewYokoma()
        self.sortInventory()

    def sellYokoma(self, index):
        sold_yokoma = self.yokoma_list.pop(index - 1)
        money = sold_yokoma.rating / 2
        self.sortInventory()
        return sold_yokoma.name, money
    
    def listYokoma(self):
        printTitle('title', "INVENTORY", 80, 0)
        for i, yokoma in enumerate(self.yokoma_list):
            rarity_color = RARITY_COLORS.get(yokoma.rarity)
            rating_color = Fore.WHITE if yokoma.rating <= 1000 else Fore.GREEN if yokoma.rating <= 10000 else Fore.YELLOW if yokoma.rating <= 100000 else Fore.LIGHTMAGENTA_EX if yokoma.rating <= 1000000 else Fore.LIGHTRED_EX if yokoma.rating <= 10000000 else Fore.RED
            printMenu(MenuItem(i + 1, Style.BRIGHT + f"{rarity_color}{yokoma.rarity} {Fore.WHITE}{yokoma.name} | {rating_color}{yokoma.rating:,}"))
        printTitle('close', "YOUR YOKOMA", 80, 0)
    
    def printNewYokoma(self):
        # get colors
        temp_yokoma = self.yokoma_list[-1]
        rarity_color = RARITY_COLORS.get(temp_yokoma.rarity)
        rating_color = Fore.WHITE if temp_yokoma.rating <= 1000 else Fore.GREEN if temp_yokoma.rating <= 10000 else Fore.YELLOW if temp_yokoma.rating <= 100000 else Fore.LIGHTMAGENTA_EX if temp_yokoma.rating <= 1000000 else Fore.LIGHTRED_EX if temp_yokoma.rating <= 10000000 else Fore.RED

        # print new yokoma
        printTitle('title', "YOUR NEW YOKOMA", 40, 0)
        printMenu(MenuItem(Style.BRIGHT + "Name", Style.BRIGHT + temp_yokoma.name))
        printMenu(MenuItem(Style.BRIGHT + "Rarity", Style.BRIGHT + rarity_color + temp_yokoma.rarity))
        printMenu(MenuItem(Style.BRIGHT + "Rating", Style.BRIGHT + f"{rating_color}{temp_yokoma.rating:,}"))
        printTitle('close', "YOUR NEW YOKOMA", 40, 0)

    def sortInventory(self):
        self.yokoma_list = sorted(self.yokoma_list, key=lambda x: x.rating, reverse=True)

    def yokomaDetail(self, index):
        # get colors
        chosen_yokoma = self.yokoma_list[index - 1]
        rarity_color = RARITY_COLORS.get(chosen_yokoma.rarity)
        rating_color = Fore.WHITE if chosen_yokoma.rating <= 1000 else Fore.GREEN if chosen_yokoma.rating <= 10000 else Fore.YELLOW if chosen_yokoma.rating <= 100000 else Fore.LIGHTMAGENTA_EX if chosen_yokoma.rating <= 1000000 else Fore.LIGHTRED_EX if chosen_yokoma.rating <= 10000000 else Fore.RED

        # print yokoma detail
        printTitle('title', chosen_yokoma.name)
        printMenu(MenuItem(Style.BRIGHT + "Rarity", Style.BRIGHT + rarity_color + chosen_yokoma.rarity))
        printMenu(MenuItem(Style.BRIGHT + "Rating", Style.BRIGHT + f"{rating_color}{chosen_yokoma.rating:,}"))
        printTitle('close', chosen_yokoma.name)
        
        return chosen_yokoma.rating / 2

    def checkYokomaExistence(self, index):
        if index <= len(self.yokoma_list):
            return True
        return False
    
    def chooseYokoma(self, index):
        return self.yokoma_list[index - 1]
    
    def getYokomaIndex(self, name):
        for index, yokoma in enumerate(self.yokoma_list):
            if yokoma.name == name:
                return index
        return -1