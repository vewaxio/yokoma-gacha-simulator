from Yokoma import Yokoma

class Combine:
    def __init__(self, yokoma1, yokoma2):
        self.yokoma1 = yokoma1
        self.yokoma2 = yokoma2
        self.yokoma_new_name = self.newNameGeneration()
        self.yokoma_new_rarity = self.newRarityGeneration()
    
    def newNameGeneration(self):
        self.new_yokoma_adjective = self.yokoma1.random_adjective + " " + self.yokoma2.random_adjective
        self.new_yokoma_animal = self.yokoma1.random_animal

        return (self.new_yokoma_adjective + " " + self.new_yokoma_animal)

    def newRarityGeneration(self):
        # Declare a value for each rarity to calculate the new rarity's leniency.
        rarity_values = {
            "Pathetic": -1,
            "Trash": 0,
            "Common": 1,
            "Uncommon": 2,
            "Rare": 3,
            "Unique": 4,
            "Legendary": 5,
            "Mythical": 6
        }

        # Get rarity values.
        rarity1 = rarity_values.get(self.yokoma1.rarity)
        rarity2 = rarity_values.get(self.yokoma2.rarity)

        # Leniency.
        self.penalty = abs(rarity1 - rarity2)

        # Calculate Compatibility.
        yokoma_name1_ascii = sum(ord(char) for char in self.yokoma1.name) / len(self.yokoma1.name)
        yokoma_name2_ascii = sum(ord(char) for char in self.yokoma2.name) / len(self.yokoma2.name)
        self.name_compatibility = abs(yokoma_name1_ascii - yokoma_name2_ascii)
        self.compatibility = self.name_compatibility - self.penalty
        
        def fetchRarityValue(target_value):
            for key, value in rarity_values.items():
                if value == target_value:
                    return key
                
        # Set new rarity.
        if self.compatibility <= 1.3:
            if self.yokoma1.rarity == "Pathetic":
                return "Pathetic"
            rarity1 -= 1
            return fetchRarityValue(rarity1)
        elif self.compatibility >= 4:
            if self.yokoma1.rarity == "Mythical":
                return "Mythical"
            rarity1 += 1
            return fetchRarityValue(rarity1)
        else:
            return self.yokoma1.rarity
    
    def returnYokoma(self):
        return Yokoma(self.yokoma_new_name, self.yokoma_new_rarity, random_adjective=self.new_yokoma_adjective, random_animal=self.new_yokoma_animal)
            

