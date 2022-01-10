def convert_time(seconds) -> str:
    minutes = int( int(seconds) / 60 )
    rem_seconds = int( int(seconds) - (minutes * 60) )
    return f"{minutes} minutter og {rem_seconds} sekunder"

with open("./resultater.dat", "r") as file:
    for line in file.readlines():
        sep_line = line.split(";")
        print(f"Deltaker {sep_line[0]}: {sep_line[1]} {sep_line[2]} {sep_line[3]} {convert_time(sep_line[4])}")
