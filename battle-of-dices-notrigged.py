from dice import *

print("🎲 Welcome to Battle of Dices! Cooler Edition 🎲")

# Variables to keep track of the score and rounds
player1_wins = 0
player2_wins = 0
round = 0
P1List = []
P2List = []

# Loop to repeat the game till someone reaches 3 points
while player1_wins < 3 and player2_wins < 3:
        
    input("\nPress ENTER to roll the dice...")
    # Player 1 rolls
    player1_roll1 = rollD6()
    player1_roll2 = rollD100()
    player1_total = player1_roll2 + player1_roll1
    P1List += [player1_total]
    print("Player 1 rolled: ", player1_total)

    # Player 2 rolls
    player2_roll1 = rollD6()
    player2_roll2 = rollD100()
    player2_total = player2_roll1 + player2_roll2
    P2List += [player2_total]
    print("Player 2 rolled: ", player2_total)
    
    input("\nPress ENTER to continue...")
    round += 1

    # deciding which Player won the round

    if player1_total > player2_total:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_total," is greater than ", player2_total)
        
    elif player1_total == player2_total:
        print("Amaaazzinng! This round has a tie!")
       
    else:
        player2_wins = player2_wins + 1
        print("Player 2 wins this round!")
        print("Because ", player2_total," is greater than ", player1_total)
        

    # Print the game score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

 # Which Player won the game
if player1_wins == 3:
    print("\nPlayer 1 is now the Master of Rolling Dice - He is the unbeatable CHAMPION")
    print("\nIt took", round, "rounds to get the Champion")
else:
    print("\nPlayer 2 is THE MASTER OF DISASTER - ROLLING DICE CHAMPION!!!")
    print("\nIt took", round,"rounds to get the Champion of Battle of DICES")

# Printing each Players rolls
print("\nPlayer 1 rolls were: ", P1List)
print("Player 2 rolls were: ", P2List)

filename = input("Enter the filename to safe the results: ")
with open(filename, "w") as file: # "w" = write mode
    for i in range(len(P1List)):
        file.write(f"Round {i+1}: Player 1 rolled {P1List}, Player 2 rolled {P2List}\n")






