teams = [
    {"lagkode": "SIL", "navn": "Smartøy Idrettslag"},
    {"lagkode": "TIL", "navn": "Turøy Idrettslag"}
]

def get_int_input(message: str) -> int:
    while True:
        try:
            user_input = int( input(message) )
            return user_input
        except ValueError:
            print("[TypeError]: Vennligst oppgi et heltall")

print("Registrering\n+==========+")

participantNr = 0
while participantNr <= 0:
    participantNr = get_int_input("Deltakernummer: ")

    if participantNr <= 0:
        print("[Error]: Deltakernummer må være større enn 0")

firstName = ""
while len(firstName) <= 1:
    firstName = input("Fornavn: ")

    if len(firstName) <= 1:
        print("[Error]: Fornavn må ha mer enn ett tegn")

lastName = ""
while len(lastName) <= 1:
    lastName = input("Etternavn: ")

    if len(lastName) <= 1:
        print("[Error]: Etternavn må ha mer enn ett tegn")

# Print all the available teams and give them an index.
# User will then choose the index number for the team they select
for i in range(len(teams)):
    print(f"{i}. {teams[i].get('lagkode')} | {teams[i].get('navn')}")

team_accepted = False
team = int()    # So that the variable "team" can be accessed outside of the while loop
while not team_accepted:
    team = get_int_input(f"Lag (0-{len(teams) - 1}): ")

    if team >= 0 and team <= (len(teams) - 1):
        team_accepted = True
    else:
        print(f"[Error]: Velg et lag fra 0 til {len(teams) - 1}")

time_sec = 0
while time_sec <= 0:
    time_sec = get_int_input("Tid (i sekunder): ")

    if time_sec <= 0:
        print("[Error]: Tid må våre større enn 0")

with open("resultater.dat", "a") as file:
    file.write(f"\n{participantNr};{firstName};{lastName};{teams[team].get('lagkode')};{time_sec}")