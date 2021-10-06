# Author: Thomas Waaler
# Programmet spørr om å oppgi to tall som deretter blir satt inn i uttrykk som viser de forskjellige operatorene i python 

print("Mini-Kalkulator")
print("Oppgi to tall for kalkulering")

# Spør bruker om input og forsikrer at ett gyldig tall er oppgitt
def get_integer_input(message: str) -> int:
    while True:
        user_input = input(message)

        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Du har ikke oppgitt ett nummer!")

number_1 = get_integer_input("Første: ")
number_2 = get_integer_input("Andre: ")

print("\n")
print(f"a *  b: {number_1 *  number_2}")
print(f"a /  b: {number_1 /  number_2}")
print(f"a +  b: {number_1 +  number_2}")
print(f"a -  b: {number_1 -  number_2}")
print(f"a %  b: {number_1 %  number_2}")
print(f"a ** b: {number_1 ** number_2}")
print(f"a // b: {number_1 // number_2}")