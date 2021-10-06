# ==================================================
# File: Oppgave_3.py
# Author: Thomas Waaler
# Info: Different ways of modifying a list
# ==================================================

tolkien_books = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

print(f"Two first books: {tolkien_books[0:2]}")
print(f"Two last books: {tolkien_books[-2:]}")

tolkien_books.append("The Silmarillion")
tolkien_books.append("Unfinished Tales")

tolkien_books[2] = "Lord of the Rings: " + tolkien_books[2]
tolkien_books[3] = "Lord of the Rings: " + tolkien_books[3]
tolkien_books[4] = "Lord of the Rings: " + tolkien_books[4]

tolkien_books.sort()

print("\n==== Tolkien books ====")
print(*tolkien_books, sep = "\n") # [1]: Print list seperated by new-line

# Kilder:
# [1]: "Print lists in Python (4 Different Ways)", Striver. URL:https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/. (13.09.2021)