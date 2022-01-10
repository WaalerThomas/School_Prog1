# A
def gjennomsnitt(tall1, tall2, tall3):
    return (tall1 + tall2 + tall3) / 3

# B
def antallNuller(array):
    antall = 0
    for i in range(len(array)):
        if array[i] == 0:
            antall += 1
    
    return antall