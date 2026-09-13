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
        """Return the list of gear names currently owned."""
        return self.diving_gear

    def check_gear_status(self):
        """Print status of every owned item (debug/console use)."""
        for gear in self.diving_gear:
            print(f"{gear}: {self.gear_status[gear]}")

    def is_broken(self, gear_name):
        """Check whether a specific owned item is broken."""
        return self.gear_status.get(gear_name) == "Broken"

    def buy_gear(self, gear_name):
        """Add a new item to the inventory if not already owned."""
        if gear_name in self.diving_gear:
            return f"{gear_name} is already in your inventory."
        self.diving_gear.append(gear_name)
        self.gear_status[gear_name] = "Working"
        return f"You bought {gear_name}!"

    def repair_gear(self, gear_name):
        """Fix a broken owned item."""
        if gear_name not in self.diving_gear:
            return f"You don't own {gear_name}."
        if self.gear_status[gear_name] == "Broken":
            self.gear_status[gear_name] = "Working"
            return f"{gear_name} has been repaired."
        return f"{gear_name} is already working."