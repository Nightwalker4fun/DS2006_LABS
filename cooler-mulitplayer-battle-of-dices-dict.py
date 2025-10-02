import copy
from dice import*
# Variables to keep track of the score
rounds = 0
gameover = False

# Number of wins needed to win the game
winning_score = 3

# Dictionary Template for storing player information
player_info = {
    "name":"",
    "email":"",
    "country":"",
    "wins": 0,
    "rolls":[]
}

# List to store the dicts for each player
players = []

# Obtain the number of players
number_of_players = int(input("How many players?"))

# For loop to obtain the player names
for i in range (number_of_players):
    # Make a deep copy of the template for this player
    player = copy.deepcopy(player_info)

    player["name"] = input(f"What is the name of Player {i+1}?")
    player["email"] = input(f"What is the e-mail of player {i+1}?")
    player["country"] = input(f"What is the country of Player {i+1}?")

    players.append(player)

while gameover is False:

    print(f"Round {rounds+1}:")
    current_rolls = []

    for each_player in players:
        roll1 = rollD6()
        roll2 = rollD8()
        total = roll1 + roll2
        round_rolls = [roll1, roll2, total]

        each_player["rolls"].append(round_rolls)

        current_rolls.append(total)

        print(f"Player {each_player['name']} rolled: {roll1} and {roll2} -> Total = {total}")

    max_roll = max(current_rolls)

    winners = []

    for each_player in players:
        if(each_player["rolls"][-1][2] == max_roll):
            each_player["wins"] += 1
            print(f"Player {each_player['name']} won in round {rounds+1}")
            winners.append(each_player['name'])

    print(f"Winners of this round: {winners}")

    for each_player in players:
        if(each_player["wins"] >= winning_score):
            print(f"\n {each_player['name']} is the newest Battle of Dices Champion!")
            gameover = True

    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

    rounds += 1

filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file: # "w" = write mode
    file.write("Player Information:\n")


    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"E-mail: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n"
        )
    file.write("\nGame rounds:\n")

    for r in range(rounds):
        rolls_str = ""

        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            if i < len(players) - 1:
                rolls_str += ", "

        file.write(f"Round {r+1}:\n {rolls_str}\n")
    print ("\nGame over! Results saved successfully.")
