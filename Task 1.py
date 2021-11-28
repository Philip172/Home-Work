#Долой IDLE! Я писал на visual studio
import random

catsPopUpPerDay = 15
dogsKilledPerDay = 0.01
k = 14.1
daysNow = 12000000

# Вычисляем количество котов
catsStartCount = random.sample(range(48000,125000), 1)[0]


a = catsPopUpPerDay*k*daysNow
countCatsOnEarth = a + catsStartCount
print("Котов в живых: " + str(countCatsOnEarth))

# Вычисляем количество собак
dogsStartCount = random.sample(range(435,666), 1)[0]
countDogsOnEarth = dogsStartCount - dogsKilledPerDay*daysNow
print("Собак в живых: " + str(countDogsOnEarth) + ' нет, все померли давно уж')
