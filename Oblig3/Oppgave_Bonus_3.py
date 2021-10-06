# ==================================================
# File: Oppgave_Bonus_3.py
# Author: Thomas Waaler
# Info: Testing file_handler module
# ==================================================
from file_handler import *

dummy_list = ["First thing", 20, True]
dummy_dict = {
    "name": "Johnsson, John",
    "age": "32",
    "job": "Accountant",
    "tasks": ["Task 1", "Task 2", "Task 3"]
}

write_list_to_file(dummy_list, "dummy_list.txt")

# A way to check if function failed
no_dummy_list = read_list_from_file("not_a_file.txt")
if not no_dummy_list:
    print(f"[Error]: Failed trying to read list from a file")

new_dummy_list = read_list_from_file("dummy_list.txt")
print(new_dummy_list)

write_dict_to_file(dummy_dict, "dummy_dict.json")

new_dummy_dict = read_dict_from_file("dummy_dict.json")
print(new_dummy_dict)