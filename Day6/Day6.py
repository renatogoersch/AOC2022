os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day6")

with open('input_day6.csv') as file:
    input_day6 = [line.rstrip() for line in file]

for i in range(3,len(input_day6[0])):
    string = input_day6[0][i-3] + input_day6[0][i-2] + input_day6[0][i-1] + input_day6[0][i]
    if len(set(string)) == 4:
        print(i+3)
        break
    