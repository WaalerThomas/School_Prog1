# ==================================================
# File: file_handler.py
# Author: Thomas Waaler
# Info: Module for handling files
# ==================================================
import json
from copy import deepcopy

def write_list_to_file(in_list: list, filename: str) -> None:
    '''Writes list elements to a file. If file already exists it will overwrite everything

    in_list: List to save to file
    filename: Name of the file to save to. Will create file where script is running from'''
    if not ".txt" in filename:
        filename = f"{filename}.txt"
    
    with open(filename, "w") as file:
        for entry in in_list:
            file.write(f"{str(entry)}\n")

def read_list_from_file(filename: str) -> list:
    '''Reads from a file and converts it to a list object. All elements will be parsed as strings
    
    filename: Name of the file to read from
    return a list of elements or 0 if error'''
    temp_list = []
    if not ".txt" in filename:
        filename = f"{filename}.txt"

    try:
        with open(filename, "r") as file:
            for line in file.readlines():
                temp_list.append(line.rstrip())
    except FileNotFoundError:
        return 0
    
    return temp_list[:]

def write_dict_to_file(in_dict: dict, filename: str) -> None:
    '''Converts a dictionary into json and saves it to a .json file
    
    in_dict: dictionary to save to file
    filename: Name of the file to save to, Will create file where script is running from'''
    if not ".json" in filename:
        filename = f"{filename}.json"
    
    with open(filename, "w") as file:
        json.dump(in_dict, file, indent=4)

def read_dict_from_file(filename: str) -> dict:
    '''Reads from a file and converts it to a dictionary object
    
    filename: Name of the file to read from
    return a dictionary or 0 if error'''
    if not ".json" in filename:
        filename = f"{filename}.json"

    try:
        with open(filename) as file:
           return json.load(file)
    except FileNotFoundError:
        return 0