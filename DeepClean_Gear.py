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