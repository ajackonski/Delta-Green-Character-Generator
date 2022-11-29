import random
class Character:
    def __init__(self, name):
        self.name = name
        self.accounting = 10
        self.alertness = 20
        self.anthropolgy = 0
        self.archeology = 0
        self.art = 0
        self.artillery = 0
        self.athletics = 30
        self.bureaucracy = 10
        self.computer_science = 0
        self.craft = 0
        self.criminology = 10
        self.demolitions = 0
        self.disguise = 10
        self.dodge = 30
        self.drive = 20
        self.firearms = 20
        self.first_aid = 10
        self.foreign_language = 0
        self.forensics = 0
        self.heavy_machinery = 10
        self.heavy_weapons = 0
        self.history = 10
        self.humint = 10
        self.law = 0
        self.medicine = 0
        self.melee_weapons = 30
        self.military_science = 0
        self.navigate = 10
        self.occult = 10
        self.persuade = 20
        self.pharmacy = 0
        self.pilot = 0
        self.psychotherapy = 10
        self.ride = 10
        self.science = 0
        self.search = 20
        self.sigint = 0
        self.stealth = 10
        self.surgery = 0
        self.survival = 10
        self.swim = 20
        self.unarmed_combat = 40
        self.unnatural = 0

    def generate_init_stats_(self):  
        self.strength = self.generate_stat()
        self.dexterity = self.generate_stat()
        self.constitution = self.generate_stat()
        self.intelligence = self.generate_stat()
        self.power = self.generate_stat()
        self.charisma = self.generate_stat()
        self.max_hit_points = (self.constitution + self.strength) // 2
        self.max_willpower_points = self.power
        self.starting_sanity_points = self.power * 5
        self.breaking_point = self.starting_sanity_points - self.power

    def generate_stat(self):
        dice_rolls = []
        current_min = random.randint(1,6)
        for k in range(1,4):
            ran_num = random.randint(1,6)
            if ran_num >= current_min:
                dice_rolls.append(ran_num)
            else:
                dice_rolls.append(current_min)
                current_min = ran_num
        final_val = sum(dice_rolls)
        return final_val
    def __str__(self):
        return f"""Your Agent\'s name is {self.name}. \nStrength: {self.strength} \nDexterity: {self.dexterity} 
Constitution: {self.constitution} \nIntelligence: {self.intelligence} \nPower: {self.power} \nCharisma: {self.charisma} 
Max HP: {self.max_hit_points} \nMax Willpower: {self.max_willpower_points} \nCurrent Sanity: {self.starting_sanity_points} \nBreaking Point: {self.breaking_point}"""