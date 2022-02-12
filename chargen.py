import random, math
class character_generator():
    def __init__(self):
        self.character_info = {"CharLevel" : 1, "Class" : "Fighter"} 
        self.ability_score_names = ["STR", "CON", "DEX", "WIS", "CHA", "INT"]
        for score in self.ability_score_names:
            self.character_info[score] = 10
        self.hit_dice_table = { # 1st Number : hitdice, 2nd number : HP per level 
            "Fighter" : [10, 6],
            "Rogue" : [8, 5],
            "Wizard" : [6, 4]
        }

    def calculate_hp(self):
        level = int(self.character_info["CharLevel"])
        char_class = self.character_info["Class"]
        CONmod = int(self.attribute_mod_from_total(self.character_info["CON"]))
        return self.hit_dice_table[char_class][0] + self.hit_dice_table[char_class][1]*(level-1) + CONmod

    def roll_dice(self, count, sides):
        sum = 0
        for i in range(count):
            sum += random.randint(1, sides)
        return sum

    def generate_attribute_rolls(self, jobclass):
        raw_attributes = []
        ability_scores = dict()
        for i in range(6):
            pre_rolls = []
            for r in range(4): # Roll 4d6 and discard the lowest die
                pre_rolls.append(self.roll_dice(1,6))
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
        for key in ability_scores:
            self.character_info[key] = ability_scores[key]
            self.character_info[key+"mod"] = self.attribute_mod_from_total(ability_scores[key])
        return ability_scores
    
    def get_stored_ability_scores(self):
        print("the values:")
        for key in self.character_info:
            print(str(key) + " : "  + str(self.character_info[key]))

    def get_pointbuy_value(self): # Works without score parameter
        scores = []
        for s in self.ability_score_names:
            scores.append(int(self.character_info[s]))
        return self.calculate_pointbuy_value(scores)

    def calculate_pointbuy_value(self, scores):
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
            if (i == 15):
                sum = sum + 9
            if (i >= 16):
                sum = sum + 12
        return sum

    def attribute_mod_from_total(self, value):
        mod = math.floor((value-10)/2)
        return str(mod) if (mod < 0) else ("+"+ str(mod))

    def create_ASCII_statblock(self):
        inf = self.character_info
        hp = self.calculate_hp()
        headline = "Unnamed  ("  + "Level " + str(inf['CharLevel']) + " " +  self.character_info['Class'] +  ") HP:" + str(hp) + "\\" + str(hp)   + "\n"
        statsline = f"""STR:{inf['STR']}({inf['STRmod']}); DEX:{inf['DEX']}({inf['DEXmod']}); CON:{inf['CON']}({inf['CONmod']}); WIS:{inf['WIS']}({inf['WISmod']}); INT:{inf['INT']}({inf['INTmod']}); CHA:{inf['CHA']}({inf['CHAmod']});"""
        return headline + statsline


