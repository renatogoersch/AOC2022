os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day6")

with open('input_day6.csv') as file:
    input_day6 = [line.rstrip() for line in file]

def get_result(block):
    for i in range((block-1),len(input_day6[0])):
        string = input_day6[0][i-(block-1):i+1]
        if len(set(string)) == block:
            print("Resultado para um word block de " + str(block) + " é: " + str(i+1))
            break

get_result(4)
get_result(14)
