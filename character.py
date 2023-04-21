import random

class Character:
    def __init__(self, name):
        self.profession = None
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
        self.craft1 = 0
        self.craft2 = 0
        self.craft3 = 0
        self.criminology = 10
        self.demolitions = 0
        self.disguise = 10
        self.dodge = 30
        self.drive = 20
        self.firearms = 20
        self.first_aid = 10
        self.foreign_language1 = 0
        self.foreign_language2 = 0
        self.foreign_language3 = 0
        self.forensics = 0
        self.heavy_machinery = 10
        self.heavy_weapons = 0
        self.history = 10
        self.humint = 10
        self.law = 0
        self.medicine = 0
        self.melee_weapons = 30
        self.military_science1 = 0
        self.military_science2 = 0
        self.military_science3 = 0
        self.navigate = 10
        self.occult = 10
        self.persuade = 20
        self.pharmacy = 0
        self.pilot = 0
        self.psychotherapy = 10
        self.ride = 10
        self.science = 0
        self.science_mathematics = 0
        self.search = 20
        self.sigint = 0
        self.stealth = 10
        self.surgery = 0
        self.survival = 10
        self.swim = 20
        self.unarmed_combat = 40
        self.unnatural = 0
        self.bonds = 0

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
Max HP: {self.max_hit_points} \nMax Willpower: {self.max_willpower_points} \nCurrent Sanity: {self.starting_sanity_points} \nBreaking Point: {self.breaking_point} \nBonds: {self.bonds} 
Skills---------------------------- \nAccounting: {self.accounting} \nAlertness: {self.alertness} \nAnthropology: {self.anthropolgy} \nArcheology: {self.archeology}
Art: {self.art} \nArtillery: {self.artillery} \nAthletics: {self.athletics} \nBureaucracy: {self.bureaucracy} \nComputer Science: {self.computer_science} \nCraft1: {self.craft1} 
Craft2: {self.craft2} \nCraft3: {self.craft3} \nCriminology: {self.criminology} \nDemolitions: {self.demolitions} \nDisguise: {self.disguise} \nDodge: {self.dodge} \nDrive: {self.drive} \nFirearms: {self.firearms} \nFirst Aid: {self.first_aid}
Foreign Language 1: {self.foreign_language1} \nForeign Language 2: {self.foreign_language2} \nForeign Language 3: {self.foreign_language3} \nForensics: {self.forensics} \nHeavy Machinery {self.heavy_machinery} 
Heavy Weapons: {self.heavy_weapons} \nHistory: {self.history} \nHUMINT: {self.humint} \nLaw: {self.law} \nMedicine: {self.medicine} \nMelee Weapons: {self.melee_weapons} \nMilitary Science1: {self.military_science1}
Navigate: {self.navigate} \nOccult: {self.occult} \nPersuade: {self.persuade} \nPharmacy: {self.pharmacy} \nPilot: {self.pilot} \nPsychotherapy: {self.psychotherapy} \nRide: {self.ride} \nScience: {self.science}
Military Science2: {self.military_science2} \nMilitary Science3: {self.military_science3} \nSearch: {self.search} \nSIGINT: {self.sigint} \nStealth: {self.stealth} \nSurgery: {self.surgery} \nSurvival: {self.survival} \nSwim: {self.swim} \nUnarmed Combat: {self.unarmed_combat} \nUnnatural: {self.unnatural}
"""   

