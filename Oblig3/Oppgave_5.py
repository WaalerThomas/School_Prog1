# ==================================================
# File: Oppgave_5.py
# Author: Thomas Waaler
# Info: Working with list of dictionaries
# ==================================================
from enum import Enum, auto

movies_list = [
    {"name":"Inception", "year":2010, "rating":8.7},
    {"name":"Inside Out", "year":2015, "rating":8.1},
    {"name":"Con Air", "year":1997, "rating":6.9},
]

class OperationMode(Enum):
    '''Enum class containing the different op-modes for use with editing movies list'''
    ADD = auto()
    CHANGE = auto()
    REMOVE = auto()

def edit_movie_list(in_list: list, name: str, year: int=2000, rating: float=5.0, operation: OperationMode=OperationMode.ADD) -> None:
    '''Adds a movie entry to the given list'''
    
    # NOTE(Tom): Does not handle duplicate entries
    # Check which operation is selected
    if operation == OperationMode.ADD:
        in_list.append( {"name":name, "year":year, "rating":rating} )
    
    elif operation == OperationMode.CHANGE:
        isFound = False
        for movie in in_list:
            if movie['name'].lower() == name.lower():
                movie['year'] = year
                movie['rating'] = rating
                isFound = True
                break   # Breaks out of the for loop
        
        if not isFound:
            print(f"[Warning]: Could not find movie with the name '{name}'")

    elif operation == OperationMode.REMOVE:
        isFound = False
        for movie in in_list:
            if movie['name'].lower() == name.lower():
                in_list.remove(movie)
                isFound = True
                break   # Breaks out of the for loop
        
        if not isFound:
            print(f"[Warning]: Could not find movie with the name '{name}'")

def print_movies(in_list: list) -> None:
    '''Prints all the movies in a given list'''
    for movie in in_list:
        print(f"\t{movie['name']} - {movie['year']} has a rating of {movie['rating']}")

def calc_average_rating(in_list: list) -> float:
    '''Calculates the average rating in given list of moives and return the result'''
    total_rating = 0.0
    for movie in in_list:
        total_rating += movie['rating']

    return (total_rating / len(in_list))

def find_movies_from(in_list: list, year: int) -> list:
    '''Find all movies from a given year and to present'''
    temp_list = []
    for movie in in_list:
        if movie['year'] >= year:
            temp_list.append(movie)
    
    return temp_list

def save_movies_to_file(in_list: list, filename: str) -> None:
    '''Save names of movies in a list and save to a file'''
    # Add .txt to the filename if it isn't specified
    if not ".txt" in filename:
        filename = f"{filename}.txt"
    
    with open(filename, "w") as file: # Will close the file at the end of with block
        for movie in in_list:
            file.write(f"{movie['name']}\n")

def read_movies_from_file(filename: str) -> None:
    '''Read movie names from a file'''
    # Add .txt to the filename if it isn't specified
    if not ".txt" in filename:
        filename = f"{filename}.txt"
    
    with open(filename, "r") as file:
        for line in file.readlines():
            print(f"\t{line}", end='')  # end='' is to remove the newline added by python

# Add some movies with the new function
edit_movie_list(movies_list, "Harry Potter and the Sorcerer's Stone", 2001, 7.6)
edit_movie_list(movies_list, "Kalashnikov", 2020, 6.6)
edit_movie_list(movies_list, "The Imitation Game", 2002, 3.0)

# Adding movie without a rating
edit_movie_list(movies_list, "Warcraft", 2016)

print("Movies in list: ")
print_movies(movies_list)

print(f"\nAverage rating: { round(calc_average_rating(movies_list), 1) }")

# Find all movies from 2010 to present
print("\nMovies from 2010 and forward:")
print_movies( find_movies_from(movies_list, 2010) )

# Save movie names to file and then read from file and print
save_movies_to_file(movies_list, "my_movies_list")
print("\nMovies from file:")
read_movies_from_file("my_movies_list")

# Bonus
edit_movie_list(movies_list, "Warcraft", operation=OperationMode.REMOVE)
edit_movie_list(movies_list, "The Imitation Game", 2014, 8.0, OperationMode.CHANGE)

print("\nMovies in list: ")
print_movies(movies_list)