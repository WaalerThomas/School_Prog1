# ==================================================
# File: Bonus_Oppgave_2.py
# Author: Thomas Waaler
# Info: "Dart game" 3.0 - 301 rule
# ==================================================
from math import floor
from random import randrange

# NOTE: An improvement could be to tell the player why they busted

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


def throw_dart(current_player_index : int, current_round_score : int) -> int:
    hit_double = False
    score_change = 0
    rand_chance = randrange(0, 101)
    max_score = scores_list[current_player_index] - current_round_score

    # NOTE: Not checking chances for 0 points since that is default
    if rand_chance >= 10 and rand_chance < 90:      # 1-20 points, Single Double and Tripple
        # max_score % 2 == 0 and 
        if max_score <= 40:  # Possible to get a double to win
            ring_point_hit = randrange(10, ((max_score / 2) * 10) + 1)
        else:
            ring_point_hit = randrange(10, 201)
        
        ring_multi_chance = randrange(0, 16)
        if ring_multi_chance >= 0 and ring_multi_chance < 2: # Tripple
            score_change = floor(ring_point_hit / 10) * 3
        elif ring_multi_chance >= 2 and ring_multi_chance < 8: # Double
            hit_double = True
            score_change = floor(ring_point_hit / 10) * 2
        elif ring_multi_chance >= 8 and ring_multi_chance < 16: # Single
            score_change = floor(ring_point_hit / 10)
        
    elif rand_chance >= 90 and rand_chance <= 100:  # Bullseye
        double_chance = randrange(0, 2)
        if double_chance == 0:  # Outer bullseye
            hit_double = True   # Double bullseye
            score_change = 50
        else:                   # Inner bullseye
            score_change = 25

    # Return 0 if it's their first throw and they didn't hit a double
    if scores_list[current_player_index] == 301 and not hit_double:
        return 0
    
    # Only check if player goes past 0 when they have 40 points or less left
    if scores_list[current_player_index] - current_round_score <= 40:
        total_score_change = current_round_score + score_change
        
        # Busted
        if (total_score_change > scores_list[current_player_index] or                                                                       # Got more than remaining points
            scores_list[current_player_index] - total_score_change == 0 and not hit_double or                                               # Got 0 points but didn't land a double
            scores_list[current_player_index] - total_score_change < 2 and scores_list[current_player_index] - total_score_change != 0):    # Score lower than lowest possible double = bust
            return -1
        elif scores_list[current_player_index] - total_score_change > 0:
            return score_change
        # Won
        elif scores_list[current_player_index] - total_score_change == 0 and hit_double:
            return -2
    
    return score_change
        

def print_scores():
    print(f"------------ Current scores -------------")
    for i in range(player_count):
        print(f"Player {i + 1} - {scores_list[i]} points")

print("========== Dart Game ==========")

current_round = 1
player_count = get_input_int("Number of players: ")
scores_list = [301 for x in range(player_count)] # List holding every players scores, starting at 301 points

while True:
    print_scores()
    print(f"\n================ Round {current_round} ================")

    for i in range(player_count):
        print(f"==== Player {i + 1}'s turn ====")
        round_score = 0
        for j in range(3): # Three throws per turn
            current_throw = throw_dart(i, round_score)

            if current_throw == -1: # Busted
                print(f"Throw {j + 1} = BUST")
                round_score = 0
                break
            elif current_throw == -2: # Won
                print(f"\n\n##### PLAYER {i + 1} WON #####")
                scores_list[i] = 0
                print_scores()
                input("Press 'Enter' to quit...")
                exit()

            round_score += current_throw
            print(f"Throw {j + 1} = {current_throw} points")

        scores_list[i] -= round_score
        print(f"Remaining points = {scores_list[i]}\n")
    
    input("Press 'Enter' to continue...")
    print("\n")         # For the looks
    current_round += 1  # End of round