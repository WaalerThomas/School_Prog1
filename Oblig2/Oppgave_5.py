# ==================================================
# File: Oppgave_5.py
# Author: Thomas Waaler
# Info: "Dart game"
# ==================================================
from random import randrange

MIN_POINTS = 0
MAX_POINTS = 60

# Get player count from user
player_count = int( input("How many are playing? ") )
if player_count <= 0:
    print("You need to specify a positive number higher than 0")
    exit(-1)

for i in range(player_count):
    print(f"\n==== Player {i + 1}'s turn ====")
    player_scores = [randrange(MIN_POINTS, MAX_POINTS + 1) for x in range(3)]   # Makes a list with three entries
    
    print(f"Throw 1: {player_scores[0]}")
    print(f"Throw 2: {player_scores[1]}")
    print(f"Throw 3: {player_scores[2]}")
    print(f"TOTAL  = {sum(player_scores)}")