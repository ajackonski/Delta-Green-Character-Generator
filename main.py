from character import Character
print("Welcome to the Delta Green Agent Generator!")
init_ = input("Would you like to generate an Agent? y/n ").lower()
if init_ == "y" or init_ == "yes":
    name = input("What is your Agent's name? ")
    agent = Character(name)
    agent.generate_init_stats_()
    print(agent)
else:
    print("Damn that sucks")