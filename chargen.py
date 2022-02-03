import random

def roll(count, sides):
    sum = 0
    for i in range(count):
        sum += random.randint(1, sides)
    return sum

def get_attribute_rolls(jobclass):
    raw_attributes = []
    ability_scores = dict()
    for i in range(6):
        pre_rolls = []
        for r in range(4): # Roll 4d6 and discard the lowest die
            pre_rolls.append(roll(1,6))
        pre_rolls.sort()
        pre_rolls.reverse()
        pre_rolls.pop()
        raw_attributes.append(pre_rolls[0] + pre_rolls[1] + pre_rolls[2])
    raw_attributes.sort()
    rand_factor = random.randint(1,5)
    if (jobclass == "Fighter"):
        priorities = ["STR", "CON", "DEX", "WIS", "CHA", "INT"]
    if (jobclass == "Wizard"):
        priorities = ["INT", "CON", "DEX", "WIS", "CHA", "STR"]
    if (jobclass == "Rogue"):
        priorities = ["DEX", "CON", "STR", "WIS", "CHA", "INT"]
    for index, p in enumerate(priorities):
        ability_scores[p] = raw_attributes.pop()
        if (index == rand_factor):
            print("Random factor " + str(rand_factor) + ". Shuffling remaining values...")
            random.shuffle(raw_attributes)
    return ability_scores

def calculate_pointbuy_value(scores):
    sum = 0
    for i in scores:
        if (i == 9):
            sum = sum + 1
        if (i == 10):
            sum = sum + 2
        if (i == 11):
            sum = sum + 3
        if (i == 12):
            sum = sum + 4
        if (i == 13):
            sum = sum + 5
        if (i == 14):
            sum = sum + 7
        if (i >= 15):
            sum = sum + 9
    return sum

class Character:
    def __init__(self, attributes):
        self.attributes = attributes
        self.stren = attributes[0]
        self.con = attributes[1]
        self.int = attributes[2]
        self.dex = attributes[3]
        self.wis = attributes[4]
        self.cha = attributes[5]
    

class Fighter(Character):
    name = "Rudolf"
    lvl = 1
    def __init__(self, attributes):
        self.attributes = attributes
        self.stren = attributes[5]
        self.con = attributes[4]
        self.dex = attributes[3]
        self.wis = attributes[2]
        self.cha = attributes[1]
        self.int = attributes[0]

def printStatBlock():
    print(" Hahah")

