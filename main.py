import random
print("Welcome to the Delta Green Agent Generator!")

def stat_generation():
    pass
    stats = ["STR", "DEX", "CON", "INT", "POW", "CHA"]
    dice_rolls = []
    for i in stats:
        current_min = random.randint(1,6)
        for k in range(1,4):
            ran_num = random.randint(1,6)
            if ran_num >= current_min:
                dice_rolls.append(ran_num)
            else:
                dice_rolls.append(current_min)
                current_min = ran_num
        final_val = sum(dice_rolls)
        print(f"{i}: {final_val}")
        dice_rolls.clear()
init_ = input("Would you like to generate an Agent? y/n ")
if init_ == "y":
    print("Your Agent's stats are:")
    stat_generation()
else:
    quit()
