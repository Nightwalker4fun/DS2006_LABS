import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")
player1__round1_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round1_roll)
player2__round1_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round1_roll)
input("\nPress ENTER to continue...")
if player1__round1_roll > player2__round1_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round1_roll == player2__round1_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 2
input("\nPress ENTER to roll the dice...")
player1__round2_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round2_roll)
player2__round2_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round2_roll)
input("\nPress ENTER to continue...")
if player1__round2_roll > player2__round2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round2_roll == player2__round2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 3
input("\nPress ENTER to roll the dice...")
player1__round3_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round3_roll)
player2__round3_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round3_roll)
input("\nPress ENTER to continue...")
if player1__round3_roll > player2__round3_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round3_roll == player2__round3_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 4
input("\nPress ENTER to roll the dice...")
player1__round4_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round4_roll)
player2__round4_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round4_roll)
input("\nPress ENTER to continue...")
if player1__round4_roll > player2__round4_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round4_roll == player2__round4_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 5
input("\nPress ENTER to roll the dice...")
player1__round5_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round5_roll)
player2__round5_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round5_roll)
input("\nPress ENTER to continue...")
if player1__round5_roll > player2__round5_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round5_roll == player2__round5_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 6
input("\nPress ENTER to roll the dice...")
player1__round6_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round6_roll)
player2__round6_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round6_roll)
input("\nPress ENTER to continue...")
if player1__round6_roll > player2__round6_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round6_roll == player2__round6_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 7
input("\nPress ENTER to roll the dice...")
player1__round7_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round7_roll)
player2__round7_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round7_roll)
input("\nPress ENTER to continue...")
if player1__round7_roll > player2__round7_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round7_roll == player2__round7_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Round 8
input("\nPress ENTER to roll the dice...")
player1__round8_roll = random.randint(1, 6)
print("Player 1 rolled: ", player1__round8_roll)
player2__round8_roll = random.randint(1, 6)
print("Player 2 rolled: ", player2__round8_roll)
input("\nPress ENTER to continue...")
if player1__round8_roll > player2__round8_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1__round8_roll == player2__round8_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Game Summary (Task 2)
print("\n-----------------------------------------")
print("| Round    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
print("-----------------------------------------")
print("| Player 1 |", player1__round1_roll, "|", player1__round2_roll, "|", player1__round3_roll, "|", player1__round4_roll, "|", player1__round5_roll, "|", player1__round6_roll, "|", player1__round7_roll, "|", player1__round8_roll, "|")
print("-----------------------------------------")
print("| Player 2 |", player2__round1_roll, "|", player2__round2_roll, "|", player2__round3_roll, "|", player2__round4_roll, "|", player2__round5_roll, "|", player2__round6_roll, "|", player2__round7_roll, "|", player2__round8_roll, "|")
print("-----------------------------------------")

# Now we need to check if either player won.
if player1_wins >= 3:
    print("Player 1 is now the Master of Rolling Dice - He is the unbeatable CHAMPION")
elif player2_wins >= 3:
    print("Player 2 is THE MASTER OF DISASTER - ROLLING DICE CHAMPION!!!")
    
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")