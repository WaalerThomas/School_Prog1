# ==================================================
# File: Oppgave_2.py
# Author: Thomas Waaler
# Info: Print a random number x times between 3 and 7
# ==================================================
from random import randint

func_call_times = randint(3, 7) # Sets how many times to call the function

# Prints a random number with some nice print
def rand_number() -> None:
    print("╔■■■■■■■■■■■■╗")
    print(f"█≡≡≡  {randint(0, 100)}  ≡≡≡█")
    print("╚■■■■■■■■■■■■╝")

# Calling the function x amount of times
for i in range(func_call_times):
    rand_number()