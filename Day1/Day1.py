os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day1")

# LOAD AND CLEAN DATA
with open('input_day1.csv') as file:
    input_day1 = [line.rstrip() for line in file]

for i in range(len(input_day1)):
    if input_day1[i] == '':
        input_day1[i] = 0
    else:
        input_day1[i] = int(input_day1[i])

max_cals = 0
cals = 0
rank = list()

for i in input_day1:
    if i > 0:
        cals = cals + i
        if cals > max_cals:
            max_cals = cals
    else:
        rank.append(cals)
        cals=0

rank.sort(reverse = True)
top3 = rank[0] + rank[1] + rank[2]
print("Resultado da Primeira Parte: " + str(max_cals))
print("Resultado da Segunda Parte: " + str(top3))