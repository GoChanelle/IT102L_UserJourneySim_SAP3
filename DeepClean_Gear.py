class Gear:
    def __init__(self):
        self.diving_gear = ["Oxygen Tank", "Diving Mask", "Flippers", "Wetsuit"]
        self.gear_status = {
            "Oxygen Tank": "Working",
            "Diving Mask": "Working",
            "Flippers": "Broken",
            "Wetsuit": "Working",
        }

    def gear_inventory(self):
        return self.diving_gear

    def check_gear_status(self):
        for gear in self.diving_gear:
            print(f"{gear}: {self.gear_status[gear]}")

    def buy_gear(self, gear_name):
        if gear_name in self.diving_gear:
            return f"{gear_name} is already in your inventory."
        self.diving_gear.append(gear_name)
        self.gear_status[gear_name] = "Working"
        return f"You bought {gear_name}!"

    def repair_gear(self, gear_name):
        if gear_name not in self.diving_gear:
            return f"You don't own {gear_name}."
        if self.gear_status[gear_name] == "Broken":
            self.gear_status[gear_name] = "Working"
            return f"{gear_name} has been repaired."
        return f"{gear_name} is already working."