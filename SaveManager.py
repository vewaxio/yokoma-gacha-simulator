import pickle, os
from Menu import Menu, printMenu, printTitle
from MenuItem import MenuItem
from colorama import Fore, Back, Style, init

class SaveManager:
    def __init__(self):
        self.save_slots = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    def save(self, data, slot_name):
        save_file_path = f"{slot_name}.sav"
        
        if os.path.exists(save_file_path):
            printTitle('title', f"Slot {slot_name} already exists. OVERWRITE?", 40, 0)
            match input("(y/n): "):
                case 'y':
                    pass
                case 'n':
                    print("\nSave canceled.")
                    return
                case _:
                    print("\nYour input is invalid.")
                    print("\nSave canceled.")
                    return
        
        with open(save_file_path, "wb") as save_file:
            pickle.dump(data, save_file)
        printTitle('title', f"Saved data to slot {slot_name}", 40, 0)

    def load(self, slot_name):
        try:
            # Deserialize and load data from the specified slot
            with open(f"{slot_name}.sav", "rb") as save_file:
                data = pickle.load(save_file)
            printMenu(MenuItem(Fore.GREEN + '+', Fore.GREEN + f"Loaded data from slot {slot_name}"))
            return data
        except FileNotFoundError:
            printMenu(MenuItem(Fore.RED + '-', Fore.RED + f"No data found in slot {slot_name}"))
            return None

    def listSaveSlots(self):
        # List available save slots and their data
        printTitle("title", "SAVE SLOTS", 40, 0)
        for slot_name in self.save_slots:
            data = self.load(slot_name)
            if data is not None:
                printMenu(MenuItem(f"Slot {slot_name}", f"{data.difficulty} {data.name} | {data.yokoyen:,} Yokoyen"))
        printTitle('close', None, 40)