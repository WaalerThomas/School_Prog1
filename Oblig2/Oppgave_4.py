# ==================================================
# File: Oppgave_4.py
# Author: Thomas Waaler
# Info: Make a list with Lord of the Rings books and print out with for-loops
# ==================================================

tolkien_books = ["The Hobbit", "Farmer Giles of Ham", "Lord of the Rings: The Fellowship of the Ring", "Lord of the Rings: The Two Towers", "Lord of the Rings: The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]
my_list = []

for book in tolkien_books:
    if "Lord of the Rings:" in book:    # Check if book contains given string
        my_list.append(book)

print("==== Lord of the Rings Trilogy: for x in y ====")
for book in my_list:
    print(book)

print("\n==== Lord of the Rings Trilogy: for i in range( len(y) ) ====")
for i in range( len(my_list) ):
    print(my_list[i])