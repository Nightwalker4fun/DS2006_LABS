from dice import *

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score and rounds
player1_wins = 0
player2_wins = 0
rounds = 0
P1rolls = []
P2rolls = []

# Loop to repeat the game till someone reaches 3 points
while player1_wins < 3 and player2_wins < 3:
        
    input("\nPress ENTER to roll the dice for Player 1...")
    player1_roll = rollD6()
    P1rolls += [player1_roll]
    print("Player 1 rolled: ", player1_roll)

    input("\nPress ENTER to roll the dice for Player 2...")
    player2_roll = rollD6()
    P2rolls += [player2_roll]
    print("Player 2 rolled: ", player2_roll)

    input("\nPress ENTER to continue...")
    rounds += 1
    # deciding which Player won the round

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
        
    elif player1_roll == player2_roll:
        print("Amaaazzinng! This round has a tie!")
        
    else:
        player2_wins = player2_wins + 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
        

    # Print the game score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

 # Which Player won the game
if player1_wins == 3:
    print("Player 1 is now the Master of Rolling Dice - He is the unbeatable CHAMPION")
    print("It took", rounds, "rounds to get the Champion")
else:
    print("Player 2 is THE MASTER OF DISASTER - ROLLING DICE CHAMPION!!!")
    print("It took", rounds,"rounds to get the Champion of Battle of DICES")

# Show the Game rolles per Player

# --- Show the Game rolls per Player in table form ---

print("-" * 50)
print("| {:8} |".format("Round"), end="")
for r in range(1, rounds+1):
    print(" {:<2}|".format(r), end="")
print()
print("-" * 50)

print("| {:8} |".format("Player 1"), end="")
for val in P1rolls:
    print(" {:<2}|".format(val), end="")
print()
print("-" * 50)

print("| {:8} |".format("Player 2"), end="")
for val in P2rolls:
    print(" {:<2}|".format(val), end="")
print()
print("-" * 50)

filename = input("Enter the filename to safe the results: ")
with open(filename, "w") as file: # "w" = write mode
    for i in range(len(P1rolls)):
        file.write(f"Round {i+1}: Player 1 rolled {P1rolls}, Player 2 rolled {P2rolls}\n")














