# ==================================================
# File: Bonus_Oppgave_1.py
# Author: Thomas Waaler
# Info: "Dart game" 2.0
# ==================================================
from random import randrange

# Function to recieve an int as input from the user with fail checking
def get_input_int(message : str) -> int:
    while True:
        try:
            user_input = int( input(message) )
            if user_input <= 0:     # Raise ValueError exception if the number is negative or 0
                raise ValueError

            return user_input
        except ValueError:
            # If given input can't be changed to an int, then this except will be called
            print("[ERROR]: You need to give a positive whole number! Please try again\n")

# "Throw" dart and get a random score
def throw_dart() -> int:
    rand_chance = randrange(0, 100 + 1)
    # 0 points
    if rand_chance >= 0 and rand_chance < 10:
        return 0

    # 1 - 20 points
    # Single, double or tripple
    if rand_chance >= 10 and rand_chance < 80:
        score = randrange(1, 21)
        score_multi_chance = randrange(0, 3)
        if score_multi_chance == 0: # Double
            return (score * 2)
        elif score_multi_chance == 1: # Single
            return score
        else: # Tripple
            return (score * 3)

    # 25 points outer bullseye
    if rand_chance >= 80 and rand_chance < 90:
        return 25

    # 50 points inner bullseye
    if rand_chance >= 90 and rand_chance <= 100:
        return 50

# Game setup
print("========== Dart Game ==========")

player_count = get_input_int("Number of players: ")
arrow_count = get_input_int("Arrows per round: ")
round_count = get_input_int("Number of rounds: ")

for i in range(round_count):
    print(f"\n==== Round {i + 1} ====")

    for j in range(player_count):
        print(f"\n==== Player {j + 1}'s turn ====")
        player_scores = [throw_dart() for x in range(arrow_count)]

        for k in range( len(player_scores) ):
            print(f"Throw {k + 1}: {player_scores[k]}")
        else:
            print(f"TOTAL = {sum(player_scores)}")