# ==================================================
# File: Oppgave_2.py
# Author: Thomas Waaler
# Info: Working with classes and methods
# ==================================================
class Movie():
    def __init__(self, title: str, release: int, score: float) -> None:
        self.title = title
        self.release = release
        self.score = score
    
    def __str__(self) -> str:
        # Method ran when trying to convert class to a str
        return f"{self.title} was released in {self.release} and has a score of {self.score}"

movies_list = []
movies_list.append( Movie("Inception", 2010, 8.8) )
movies_list.append( Movie("The Martian", 2015, 8.0) )
movies_list.append( Movie("Joker", 2019, 8.4) )

print("Printing from loop:")
for movie in movies_list:
    print(f"{movie.title} was released in {movie.release} and has a score of {movie.score}")

print("\nPrinting from method:")
print(*movies_list, sep="\n")   # * will turn all items into str elements instead of printing class information