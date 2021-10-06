# Author: Thomas Waaler
# Legger sammen totalt hvor mange småkaker som har blitt spist og deretter regner ut gjennomsnittet

eaten_cookies = [ 5, 9, 2.5, 21, 0 ]
people_count = len(eaten_cookies)
total_eaten = sum(eaten_cookies)

average = int(total_eaten / people_count) # Casting to int will floor the result
print(average)