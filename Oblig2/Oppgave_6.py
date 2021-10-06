# ==================================================
# File: Oppgave_6.py
# Author: Thomas Waaler
# Info: Program to make a packing list with the possibility to add and remove items
# ==================================================

is_running = True
packing_list = []

print("==============================")
print("==== Packing list creator ====")
print("==============================")
while is_running:
    print("Choices:")
    print("\t1. Add item\n\t2. Remove item\n\t3. List items\n\n\t0. Quit Program\n")

    user_input = int( input("Choose an option (0-3): ") )
    if user_input < 0 or user_input > 3:
        print(f"- {user_input} isn't an option. Please try again!\n")
        continue

    # Comes here when user_input is accepted
    # Quit program
    if (user_input == 0):
        is_running = False

    # Add item
    elif (user_input == 1):
        item_to_add = input("\nWhat are you adding? ")
        packing_list.append(item_to_add)
        packing_list.sort()
        print(f"- Added item '{item_to_add}' to the list\n")

    # Remove item
    elif (user_input == 2): 
        if len(packing_list) <= 0:
            print("- List doesn't contain anything yet. Please add something first\n")
            continue
        
        item_to_remove = int( input("\nRemove item by specifying it's index, can be found by listing items (0 to cancel): ") )
        if item_to_remove == 0:
            print("- Cancelled remove command\n")
            continue
        elif (item_to_remove - 1) >= 0 and (item_to_remove - 1) < len(packing_list):
            print(f"- Removed item '{packing_list[item_to_remove - 1]}' from the list\n")
            del packing_list[item_to_remove - 1]
        else:
            print(f"- {item_to_remove} isn't an index in the list\n")

    # List items  
    elif (user_input == 3):
        if len(packing_list) <= 0:
            print("- List doesn't contain anything yet. Please add something first\n")
            continue

        print("\n==== Items ====")
        for i in range( len(packing_list) ):
            print(f"{i + 1}: {packing_list[i]}")
        print("") # For making the output more pretty