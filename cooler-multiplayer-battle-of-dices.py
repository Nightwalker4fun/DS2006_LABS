from dice import*

# Number of wins needed to win the game
winning_score = 3
rounds = 0
gameover = False
# Array for storing the names of the players
player_names = []
# Array for storing the number of wins for each player
player_wins = []
# Obtain the number of players
number_of_players = int(input("How many players?"))
# For loop to obtain the player names
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?")
    player_names.append(name)
# Initialize scres and rolls
for i in range (number_of_players):
    player_wins.append(0)
# Initialize player rolls as empty lists for each player
player_rolls_history = [] # This will be  a nested list
for i in range (number_of_players):
    # Add an empty list for each player
    player_rolls_history.append([])
# Repeats until the game is over. As many rounds as necessary
while gameover is False:
    print(f"Round {rounds+1}:")

    # Dice roll for each player in the current round
    current_rolls = []

    # We need to roll the dice for each player
    for i in range(number_of_players):
        roll1 = rollD6()
        roll2 = rollD8()
        roll = roll1 + roll2
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled: {roll}")
    input("\nPress ENTER to continue...")

    # Obtain the highest roll this round:
    max_roll = max(current_rolls)

    #winners will store information abow who won this round
    winners = []

    # Search for all players who got the highest roll
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    print(f"Winners of this round are: {winners}")

    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n {player_names[z]} is the newest Battle of Dices Champion!")
            gameover = True
    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end?")
    rounds += 1

# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = " "
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_rolls_history[i][round_number]}")
            if i < number_of_players - 1:
                rolls_str += " "
        print(f"Saving {rolls_str}")

        file.write(rolls_str + "\n")

