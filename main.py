from character import Character
print("Welcome to the Delta Green Agent Generator!")
name = input("What is your Agent's name? ")
agent = Character(name)
agent.generate_init_stats_()
print(agent)
