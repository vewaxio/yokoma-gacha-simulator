import random
import math

class Yokoma:
    def __init__(self, name = None, rarity = None, rating = None, random_adjective = None, random_animal = None):
        self.random_adjective = random_adjective
        self.random_animal = random_animal
        self.name = name or self.generateName()
        self.rarity = rarity or self.generateRarity()
        self.rating = rating or self.generateRating()
    
    def generateName(self):
        # Load required resources to generate a randomized name.
        with open('Adjectives.txt', 'r') as adjectives_file:
            adjectives = adjectives_file.read().splitlines()

        with open('Animals.txt', 'r') as animals_file:
            animals = animals_file.read().splitlines()

        # Generate a randomized name.
        self.random_adjective = random.sample(adjectives, 1)[0].title()
        self.random_animal = random.sample(animals, 1)[0].title()

        return self.random_adjective + " " + self.random_animal

    def generateRarity(self):
        # Generate the rarity based on probability.
        generated_rarity = random.choices(["Trash", "Common", "Uncommon", "Rare", "Unique", "Legendary"], weights = (15, 60, 20, 3, 1.7, 0.3))[0]
        return generated_rarity

    def generateRating(self):
        # Generate the rating multiplier based on rarity.
        def getRatingMultiplier(rarity):
            match rarity:
                case "Pathetic":
                    temp_multiplier = 0.05
                case "Trash":
                    temp_multiplier = 0.3
                case "Common":
                    temp_multiplier = 1
                case "Uncommon":
                    temp_multiplier = 1.5
                case "Rare":
                    temp_multiplier = 2
                case "Unique":
                    temp_multiplier = 3.5
                case "Legendary":
                    temp_multiplier = 7
                case "Mythical":
                    temp_multiplier = 25
                
            return temp_multiplier
                
        rating_multiplier = getRatingMultiplier(self.rarity)

        # Generate the rating using ASCII.
        ascii_values = [ord(char) for char in self.name]

        return math.ceil(sum(ascii_values) * rating_multiplier)