class CreatureCollection:
    def __init__(self):
        # Master list of all creatures in the game
        self.creatures = {
            "Oil Specter": {"description": "Elusive and shiny. :red[But being near makes you choke.]", "collected": False},
            "Cigar Filters": {"description": "Small yet many. :red[It's hard to see when a hoard is near.]", "collected": False},
            "Film Wrapper": {"description": "Drifts with purpose. :red[They'll choke you out.].", "collected": False},
            "Fishing Gear": {"description": "There is fishing gear here? :red[Those hooks look like they hurt.].", "collected": False},
            "Pallid Whale": {"description": "Heaps of trash that turn into an amalgamation. :red[The infection spreads.]", "collected": False},
        }

    def get_all(self):
        return self.creatures

    def get_uncollected(self):
        return [name for name, info in self.creatures.items() if not info["collected"]]

    def get_collected(self):
        return [name for name, info in self.creatures.items() if info["collected"]]

    def collect(self, name):
        if name not in self.creatures:
            return f"{name} isn't a known creature."
        if self.creatures[name]["collected"]:
            return f"You've already collected {name}."
        self.creatures[name]["collected"] = True
        return f"You collected {name}!"

    def is_collected(self, name):
        return self.creatures.get(name, {}).get("collected", False)