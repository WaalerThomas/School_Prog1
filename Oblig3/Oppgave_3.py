# ==================================================
# File: Oppgave_3.py
# Author: Thomas Waaler
# Info: Print each element in a list with a function
# ==================================================
def print_list(in_list: list) -> None:
    print("Printing list:")
    for item in in_list:
        print(f"- {item}")

fav_animals = ["Ferret", "Weasel", "Red panda"]
print_list(fav_animals)