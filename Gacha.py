from Yokoma import Yokoma

class Gacha:
    def __init__(self):
        self.pull_count = 0
        self.pity_counters = {
            "Rare": 0,
            "Unique": 0,
            "Legendary": 0
        }
        self.pity_thresholds = {
            "Rare": 10,
            "Unique": 50,
            "Legendary": 150
        }

    def onePull(self):
        self.pull_count += 1
        self.pity_counters = {key: value + 1 for key, value in self.pity_counters.items()}

        # Check whether pity threshold has been reached.
        for check_rarity in self.pity_counters:
            if self.pity_counters[check_rarity] >= self.pity_thresholds[check_rarity]:
                self.pity_counters[check_rarity] = 0
                return Yokoma(rarity = check_rarity)

        # Do a normal pull
        yokoma = Yokoma()
        if yokoma.rarity in self.pity_counters:
            self.pity_counters[yokoma.rarity] = 0
        return yokoma