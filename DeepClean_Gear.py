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
        for item in self.diving_gear:
            if item["name"] == gear_name:
                return f"{gear_name} is already in your inventory."

        self.diving_gear.append({"name": gear_name, "status": "Working"})
        return f"You bought {gear_name}!"

    def repair_gear(self, gear_name):
        for item in self.diving_gear:
            if item["name"] == gear_name:
                if item["status"] == "Broken":
                    item["status"] = "Working"
                    return f"{gear_name} has been repaired."
                else:
                    return f"{gear_name} is already working."
        return f"You don't own {gear_name}."