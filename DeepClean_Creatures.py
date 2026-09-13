class CreatureCollection:
    def __init__(self):
        # Master list of all creatures in the game
        self.creatures = {
            "Clownfish": {"description": "Small, orange, hides in anemones.", "collected": False},
            "Sea Turtle": {"description": "Ancient wanderer of the reef.", "collected": False},
            "Jellyfish": {"description": "Drifts with the current, watch the sting.", "collected": False},
            "Octopus": {"description": "Master of disguise.", "collected": False},
            "Trash Beast": {"description": "A creature born from ocean pollution.", "collected": False},
        }

    def get_all(self):
        """Return every creature and its state."""
        return self.creatures

    def get_uncollected(self):
        """Return only creatures not yet collected — used for Dive encounters."""
        return [name for name, info in self.creatures.items() if not info["collected"]]

    def get_collected(self):
        """Return only creatures already collected — used for the Index."""
        return [name for name, info in self.creatures.items() if info["collected"]]

    def collect(self, name):
        """Mark a creature as collected."""
        if name not in self.creatures:
            return f"{name} isn't a known creature."
        if self.creatures[name]["collected"]:
            return f"You've already collected {name}."
        self.creatures[name]["collected"] = True
        return f"You collected {name}!"

    def is_collected(self, name):
        return self.creatures.get(name, {}).get("collected", False)