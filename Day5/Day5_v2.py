os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day5")

with open('input_day5.csv') as file:
    input_day5 = [line.rstrip() for line in file]

with open('input_day5_2.csv') as file:
    input_day5_2 = [line.rstrip() for line in file]

endline = 0

for n in range(len(input_day5_2)):
    if '1' in input_day5_2[n]:
        endline = n

def create_stacks():
    stacks = []
    for i in range(endline+1):
        newstack = []
        for n in range(len(input_day5_2)-1):
            if (1+(4*i)) > len(input_day5_2[n]):
                letter = ' '
            else:
                letter = input_day5_2[n][1+(4*i)]
            newstack.insert(0, letter)
        while ' ' in newstack:
            newstack.remove(' ')
        #stacks.append(newstack)
        stacks.append(list(reversed(newstack)))
    return stacks

    
def move(qtd,wfrom,wto,stacks):
    #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
    for i in range(qtd):
        to_move = stacks[wfrom-1][0]
        stacks[wfrom-1].pop(0)
        stacks[wto-1].insert(0, to_move)

def move2(qtd,wfrom,wto,stacks):
    #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
    s_to_move = stacks[wfrom-1][0:qtd]
    for i in range(qtd):
        to_move = s_to_move[-1]
        s_to_move.pop(-1)
        stacks[wfrom-1].pop(len(s_to_move))
        stacks[wto-1].insert(0, to_move)

stacks = create_stacks()
for n in input_day5:
    values = n.split(' ')
    move(int(values[1]),int(values[3]),int(values[5]),stacks)

result = stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0]
print("Resultado da Primeira Parte: " + str(result))
    
stacks = create_stacks()
for n in input_day5:
    values = n.split(' ')
    move2(int(values[1]),int(values[3]),int(values[5]),stacks)

result = stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0]
print("Resultado da Segunda Parte: " + str(result))
