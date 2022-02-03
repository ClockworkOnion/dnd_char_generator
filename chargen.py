import random

def roll(count, sides):
    sum = 0
    for i in range(count):
        sum += random.randint(1, sides)
    return sum

def get_attribute_rolls():
    attributes = []
    for i in range(6):
        pre_rolls = []
        for r in range(4):
            pre_rolls.append(roll(1,6))
        pre_rolls.sort()
        pre_rolls.reverse()
        pre_rolls.pop()
        attributes.append(pre_rolls[0] + pre_rolls[1] + pre_rolls[2])
    attributes.sort()
    return attributes

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

def main():
    att = get_attribute_rolls()
    guy = Fighter(att)
    print(guy.attributes)
    print(guy.getStrMod())
    print(guy.getMod("dex"))


main()