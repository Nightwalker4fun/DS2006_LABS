import random

input("Press Enter to roll the Dice")

# Roll the dice
result = random.randint(1, 20)

# Show the result
print("You rolled a", result, "out of D20")

def rollD4():
    return random.randint(1, 4)

def rollD6():
    return random.randint(1, 6)

def rollD8():
    return random.randint(1, 8)

def rollD12():
    return random.randint(1, 12)

def rollD20():
    return random.randint(1, 20)

def rollD100():
    return random.randint(1, 100)