from dice import *

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score and rounds
player1_wins = 0
player2_wins = 0
round = 0

# Loop to repeat the game till someone reaches 3 points
while player1_wins < 3 and player2_wins < 3:
        
    input("\nPress ENTER to roll the dice...")

    player1_roll = rollD6()
    print("Player 1 rolled: ", player1_roll)

    player2_roll = rollD6()
    print("Player 2 rolled: ", player2_roll)

    input("\nPress ENTER to continue...")

    # deciding which Player won the round

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
        round += 1
    elif player1_roll == player2_roll:
        print("Amaaazzinng! This round has a tie!")
        round += 1
    else:
        player2_wins = player2_wins + 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
        round += 1

    # Print the game score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

 # Which Player won the game
if player1_wins == 3:
    print("Player 1 is now the Master of Rolling Dice - He is the unbeatable CHAMPION")
    print("It took", round, "rounds to get the Champion")
else:
    print("Player 2 is THE MASTER OF DISASTER - ROLLING DICE CHAMPION!!!")
    print("It took", round,"rounds to get the Champion of Battle of DICES")












