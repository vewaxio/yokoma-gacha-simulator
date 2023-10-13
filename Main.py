import time
import sys
import random
from Profile import Profile
from Gacha import Gacha
from Combine import Combine
from Inventory import Inventory
from Achievement import Achievement
from SaveManager import SaveManager
from Menu import Menu, printMenu, printTitle
from MenuItem import MenuItem

def loadingAnimation():
    width = 40  # Width of the loading bar
    for i in range(width + 1):
        progress = i / width
        bar = "#" * i
        spaces = " " * (width - i)
        # Calculate color transition
        red_value = 255 - int(255 * progress)
        green_value = int(255 * progress)
        # Set foreground color
        color = f"\x1b[38;2;{red_value};{green_value};0m"
        print(
            f"{color}[{bar}{spaces}] {int(progress * 100)}%",
            end="\r",
            flush=True,
        )
        time.sleep(0.1)
    print()

def gacha(player):
    while True:
        updateAchievement(player)
        Menu.printGacha()
        match input("Your choice: "):
            case '1':
                if player.yokoyen >= 1000:
                    player.yokoyen -= 1000
                    temp_yokoma = player.gacha.onePull()
                    player.inventory.addYokoma(temp_yokoma)
                else:
                    print("You don't have enough Yokoyen.")
            case '2':
                if player.yokoyen >= 10000:
                    player.yokoyen -= 10000
                    print("\nDoing a 10 pull..")
                    time.sleep(1)
                    for _ in range(10):
                        temp_yokoma = player.gacha.onePull()
                        player.inventory.addYokoma(temp_yokoma)
                        time.sleep(0.3)
                    updateAchievement(player)
                else:
                    print("You don't have enough Yokoyen.")
                    updateAchievement(player)
            case '3':
                count = 0
                try:
                    amount = int(input("Amount: "))
                    if amount > 100:
                        printTitle('title', "BULK GACHA TIME")
                        loadingAnimation()
                    for _ in range (amount):
                        if player.yokoyen >= 1000:
                            count += 1
                            player.yokoyen -= 1000
                            temp_yokoma = player.gacha.onePull()
                            player.inventory.addYokoma(temp_yokoma)
                            if amount <= 100:
                                time.sleep(0.1)
                        updateAchievement(player)
                    printTitle('title', f"You pulled {count} time(s)!")
                    updateAchievement(player)
                except ValueError:
                    print("\nYou didn't input an integer.")
            case 'q':
                break
            case _:
                print("Please input a valid choice.")

def bulkSellYokoma(player, input_indices):
    indices = input_indices.split(',')  # split the input into a list of indices
    indices = [int(index.strip()) for index in indices]  # convert and clean the input

    # remove duplicates from the list
    unique_indices = list(set(indices))

    # sort the unique indices in descending order
    unique_indices.sort(reverse=True)

    sell_names = []  # list to store the names of the sold Yokoma
    total_sell_money = 0

    for index in unique_indices:
        try:
            if 0 <= index < len(player.inventory.yokoma_list) + 1:
                sell_name, sell_money = player.inventory.sellYokoma(index)
                sell_names.append(sell_name)
                total_sell_money += sell_money
            else:
                print(f"Invalid index: {index}")
        except ValueError:
            print(f"Invalid input: {index}")

    if total_sell_money > 0:
        printTitle('title', "SOLD", 80, 0)
        for yokoma in sell_names:
            printMenu(MenuItem('-', yokoma))
        printTitle('close', None, 80)
        player.accumulated_yokoyen += total_sell_money
        player.yokoyen += total_sell_money
        updateAchievement(player)
        printTitle('title', f"You have received {total_sell_money:,} Yokoyen!")
    else:
        print("No Yokoma were sold.")

    if player.yokoyen < 1000 and len(player.inventory.yokoma_list) == 0:
        time.sleep(5)
        printTitle('title', "GAME OVER", 40, 0)
        printMenu(MenuItem('-', "Uh oh! You've run out of money and Yokoma. The game is now over, you fought valiantly!"))
        printMenu(MenuItem('-', "I will now show you your legacy."))
        printTitle('close', None, 40, 0)
        player.printProfile()
        sys.exit()

def inventory(player):
    while True:
        player.inventory.listYokoma()
        Menu.printInventory()
        match input("Your choice: "):
            case '1':
                printTitle('title', "CHOOSE YOKOMA BY INDEX")
                try:
                    index = int(input())
                    if (player.inventory.checkYokomaExistence(index)):
                        player.inventory.yokomaDetail(index)
                        pass
                    else:
                        print("Your choice doesn't exist.")
                except ValueError:
                    print("\nPlease input an integer.")
            case '2':
                combine(player)
            case '3':
                printTitle('title', "SELL", 80, 0)
                bulkSellYokoma(player, input("Enter the indices of the Yokoma you want to sell, separated by commas: "))
            case '4':
                combine(player, 'bulk')
            case 'q':
                break
            case _:
                print("\nPlease input a valid choice.")

def combine(player, type = None):
    try:
        if type != 'bulk':
            printTitle('title', "Please note that the first Yokoma is prioritized when combining.")
            while True:
                index1 = int(input("Choose the first Yokoma: "))
                index2 = int(input("Choose the second Yokoma: "))
                if index1 == index2:
                    print("\nYou cannot combine two of the same Yokoma!")
                    continue
                break
            if player.inventory.checkYokomaExistence(index1) and player.inventory.checkYokomaExistence(index2):
                printTitle('title', "CONFIRMATION")
                player.inventory.yokomaDetail(index1)
                player.inventory.yokomaDetail(index2)
                confirmation = input("Would you like to combine these two Yokoma? (y/n): ")
                match confirmation:
                    case 'y':
                        combined_yokoma = Combine(player.inventory.chooseYokoma(index1), player.inventory.chooseYokoma(index2)).returnYokoma()
                        if index1 < index2:
                            index1, index2 = index2, index1
                        player.inventory.sellYokoma(index1)
                        player.inventory.sellYokoma(index2)
                        player.inventory.addYokoma(combined_yokoma)
                        player.combination_count += 1
                        updateAchievement(player)
                        time.sleep(0.5)
                    case 'n':
                        pass
                    case _:
                        print("\nPlease input a valid choice.")
        else:
            yokoma_to_combine = []
            printTitle('title', "BULK COMBINE")
            while True:
                input_indices = input("Choose the Yokoma(s) separated by commas: ")
                indices = input_indices.split(',')  # split the input into a list of indices
                indices = [int(index.strip()) for index in indices]  # convert and clean the input

                # remove duplicates from the list
                unique_indices = list(set(indices))

                # sort the unique indices in descending order
                unique_indices.sort(reverse=True)
                break
            loadingAnimation
            for index in unique_indices:
                if player.inventory.checkYokomaExistence(index):
                    yokoma_to_combine.append(player.inventory.chooseYokoma(index))
                    player.inventory.sellYokoma(index)
                else:
                    print(f"Invalid index: {index}")
            while True:
                if len(yokoma_to_combine) == 1:
                    player.inventory.addYokoma(yokoma_to_combine[0])
                    break
                combined_yokoma = Combine(yokoma_to_combine[0], yokoma_to_combine[1]).returnYokoma()
                yokoma_to_combine[0] = combined_yokoma
                del yokoma_to_combine[1]
                player.combination_count += 1
                updateAchievement(player)
    except ValueError:
        print("\nPlease input an integer.")

def updateAchievement(player):
    for achievement in player.achievement.achievements:
        if achievement["ID"] in [1, 2, 3, 4, 5]:
            achievement ["progress"] = player.gacha.pull_count
        elif achievement["ID"] in [6, 7, 8, 9, 10]:
            achievement["progress"] = player.accumulated_yokoyen
        elif achievement["ID"] in [11, 12, 13, 14]:
            achievement["progress"] = player.combination_count
        player.achievement.updateProgress()

def onboarding():
    print("\nHello, user! Welcome to the wonderful world of Gacha Simulator.")
    print("Before you proceed, please make sure you understand how this game works. (Refer to the readme.txt file if you are still confused)")
    while True:
        Menu.printOnboarding()
        choice = input("Your choice: ")
        match choice:
            case '1':
                newGame()
            case '2':
                player = saveManager(action = "load")
                if player != None:
                    startGame(player)
            case 'q':
                print("\nI await your return!")
                break
            case _:
                print("\nPlease input a valid choice.")

def newGame():
    printTitle("title", "PLEASE INPUT YOUR NAME")
    player_name = input("Your name: ")
    while True:
        Menu.printDifficultyChoice()
        choice = input("Your choice: ")
        match choice:
            case '1':
                yokoyen = 100000
                difficulty = "Baby"
                break
            case '2':
                yokoyen = 50000
                difficulty = "Casual"
                break
            case '3':
                yokoyen = 20000
                difficulty = "Challenger"
                break
            case '4':
                yokoyen = 10000
                difficulty = "Demonic"
                break
            case _:
                print("Please input a valid choice.")
    printTitle('title', "GENERATING USER PROFILE", 40, 0)
    loadingAnimation()
    gacha = Gacha()
    inventory = Inventory()
    achievement = Achievement()
    player = Profile(player_name, yokoyen, gacha, inventory, achievement, difficulty)
    time.sleep(1)
    startGame(player)

def saveManager(player = {}, action = ""):
    if action == "save":
        while True:
            save_manager.listSaveSlots()
            match input("Save to which slot? (1-10/q): "):
                case '1':
                    save_manager.save(player, 1)
                    break
                case '2':
                    save_manager.save(player, 2)
                    break
                case '3':
                    save_manager.save(player, 3)
                    break
                case '4':
                    save_manager.save(player, 4)
                    break
                case '5':
                    save_manager.save(player, 5)
                    break
                case '6':
                    save_manager.save(player, 6)
                    break
                case '7':
                    save_manager.save(player, 7)
                    break
                case '8':
                    save_manager.save(player, 8)
                    break
                case '9':
                    save_manager.save(player, 9)
                    break
                case '10':
                    save_manager.save(player, 10)
                    break
                case 'q':
                    break
                case _:
                    print("\nPlease input a valid choice.")
    elif action == "load":
        while True:
            save_manager.listSaveSlots()
            match input("Load which slot? (1-10/q): "):
                case '1':
                    return save_manager.load(1)
                case '2':
                    return save_manager.load(2)
                case '3':
                    return save_manager.load(3)
                case '4':
                    return save_manager.load(4)
                case '5':
                    return save_manager.load(5)
                case '6':
                    return save_manager.load(6)
                case '7':
                    return save_manager.load(7)
                case '8':
                    return save_manager.load(8)
                case '9':
                    return save_manager.load(9)
                case '10':
                    return save_manager.load(10)
                case 'q':
                    break
                case _:
                    print("\nPlease input a valid choice.")

def startGame(player):
    while True:
        Menu.printMainMenu(player.yokoyen)
        match input("Your choice: "):
            case '1':
                player.printProfile()
            case '2':
                gacha(player)
            case '3':
                inventory(player)
            case '4':
                player.achievement.listAchievements()
                while True:
                    printMenu(MenuItem('q', "Return"))
                    choice = input("Your choice: ")
                    match choice:
                        case 'q':
                            break
                        case _:
                            print("\nPlease input a valid choice.")
            case '5':
                saveManager(player, "save")
            case 'q':
                print(f"\nI'm looking forward to your return, {player.name}!")
                break
            case _:
                print("\nPlease input a valid choice.")

if __name__ == "__main__":
    save_manager = SaveManager()
    onboarding()