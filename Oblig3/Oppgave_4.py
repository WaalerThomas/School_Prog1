# ==================================================
# File: Oppgave_4.py
# Author: Thomas Waaler
# Info: Function to calculate the circumference of a rectangle
# ==================================================
def calc_circumference(length: float, width: float) -> float:
    return (length * 2 + width * 2)

# To see that the function is "functional" XD
print(f"Rectangle - L:20.0 W:50.0 C:{calc_circumference(20.0, 50.0)}")
print(f"Rectangle - L:400.0 W:15.75 C:{calc_circumference(400.0, 15.75)}")