import math
import random

class Character:

    def ability(self):
        random.seed()
        rolls=[random.randint(1,6), random.randint(1,6),
               random.randint(1,6), random.randint(1,6)]
        return (sum(rolls)-min(rolls))

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

def modifier(stat: int) -> int:
    return math.floor((stat-10)/2)