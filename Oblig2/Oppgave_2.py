# ==================================================
# File: Oppgave_2.py
# Author: Thomas Waaler
# Info: Lists all the odd numbers from 9 to 101 with a for-loop then a while-loop
# ==================================================

start_number = 9
end_number = 101

odd_for_list = []   # Makes it look nicer when printed to the console
for i in range(start_number, end_number + 1):
    if i % 2 != 0:  # If number can't be divided by two
        odd_for_list.append(i)

print(f"==== Odd numbers - For-loop: {len(odd_for_list)} entries ====")
print(odd_for_list)

odd_while_list = []   # Makes it look nicer when printed to the console
i = start_number
while i <= end_number:
    if i % 2 != 0:  # If number can't be divided by two
        odd_while_list.append(i)

    i += 1

print(f"\n==== Odd numbers - While-loop: {len(odd_while_list)} entries ====")
print(odd_while_list)