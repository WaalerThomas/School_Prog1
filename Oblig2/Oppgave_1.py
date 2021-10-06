# ==================================================
# File: Oppgave_1.py
# Author: Thomas Waaler
# Info: Simple example of if, elif and else usage
# ==================================================

user_input = input("Hva er meningen med livet? ")
user_input = int(user_input)

if user_input == 42:
    print("Det stemmer, meningen med livet er 42!")
elif user_input > 30 and user_input < 50:
    print("Nærme, men feil.")
else:
    print("FEIL!")