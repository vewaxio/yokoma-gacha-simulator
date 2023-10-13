from MenuItem import MenuItem
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def printTitle(type, text = None, text_length = None, padding_left = 3):
    text_length = len(text) + 4 if text_length == None else text_length
    text_length = 80 if text_length > 80 else text_length
    line = Style.BRIGHT + "+" + "-" * (text_length) + "+"
    if type == "title":
        print()
        print(line)
        if padding_left == 0:
            padding_left = int(((text_length + 2) - len(text)) / 2)
        print(" " * padding_left + Fore.CYAN + Style.BRIGHT + text)
        print(line)
    elif type == "close":
        
        print(line)

def printMenu(menu_item, color = Fore.WHITE):
    print(f"   {Fore.YELLOW}{Style.BRIGHT}({Style.RESET_ALL}{color}{menu_item.index}{Fore.YELLOW}{Style.BRIGHT}): {Style.RESET_ALL}{color}{menu_item.text}")

class Menu:
    def printMainMenu(yokoyen):
        printTitle("title", f"MAIN MENU {Fore.WHITE}| {Fore.GREEN if yokoyen >= 10000 else Fore.RED}You Have {yokoyen:,} Yokoyen", 55)
        printMenu(MenuItem(1, "Check Profile"))
        printMenu(MenuItem(2, "Gacha"))
        printMenu(MenuItem(3, "Inventory"))
        printMenu(MenuItem(4, "Achievements"))
        printMenu(MenuItem(5, "Save"))
        printMenu(MenuItem('q', "Quit"))
        printTitle("close", None, 55, 0)

    def printDifficultyChoice():
        printTitle("title", "CHOOSE YOUR DIFFICULTY", len("Challenger | You'll start with 20,000 Yokoyen") + 9, 0)
        printMenu(MenuItem(1, "Baby | You'll start with 100,000 Yokoyen"), Fore.GREEN)
        printMenu(MenuItem(2, "Casual | You'll start with 50,000 Yokoyen"), Fore.LIGHTBLUE_EX)
        printMenu(MenuItem(3, "Challenger | You'll start with 20,000 Yokoyen"), Fore.YELLOW)
        printMenu(MenuItem(4, "???"), Fore.RED)
        printTitle("close", None, len("Challenger | You'll start with 20,000 Yokoyen") + 9)

    def printOnboarding():
        printTitle("title", "GACHA SIMULATOR - YOKOMA")
        printMenu(MenuItem(1, "New Game"))
        printMenu(MenuItem(2, "Continue"))
        printMenu(MenuItem('q', "Quit"))
        printTitle("close", "GACHA SIMULATOR - YOKOMA")

    def printGacha():
        printTitle("title", "YOKOMA GACHA", 24 + 6, 0)
        printMenu(MenuItem(1, "Pull 1 Yokoma"))
        printMenu(MenuItem(2, "Pull 10 Yokoma"))
        printMenu(MenuItem(3, "Specify an amount"))
        printMenu(MenuItem('q', "Return to Main Menu"))
        printTitle("close", "YOKOMA GACHA", 24 + 6)

    def printInventory():
        printTitle("title", "INVENTORY", 30, 0)
        printMenu(MenuItem(1, "Check a Yokoma"))
        printMenu(MenuItem(2, "Combine Yokoma"))
        printMenu(MenuItem(3, "Sell Yokoma(s)"))
        printMenu(MenuItem(4, "Bulk Combine"))
        printMenu(MenuItem('q', "Return"))
        printTitle("close", "INVENTORY", 30, 0)
