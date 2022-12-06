os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day5")

with open('input_day5.csv') as file:
    input_day5 = [line.rstrip() for line in file]

with open('input_day5_2.csv') as file:
    input_day5_2 = [line.rstrip() for line in file]

maxl = 0
for n in range(len(input_day5_2)):
    if len(input_day5_2[n]) > maxl:
        maxl = len(input_day5_2[n])

nstacks = round(maxl/4)
endline = 0

for n in range(len(input_day5_2)):
    if '1' in input_day5_2[n]:
        endline = n

stacks2 = []
for n in range(endline):
    newstack = []
    for i in range(len(input_day5_2)):
        if (1+(4*i)) > len(input_day5_2[n]):
            letter = ' '
        else:
            letter = input_day5_2[n][1+(4*i)]
        newstack.insert(0, letter)
    while ' ' in newstack:
        newstack.remove(' ')
    print(newstack)
    stacks2.append(list(reversed(newstack)))

for n in range(len(input_day5_2)):
    stacks = []
    newstack = []
    for i in range(round(len(input_day5_2[n])/4)):
        letter = input_day5_2[n][len(input_day5_2[n])-(2+(i*4))]
        newstack.insert(0, letter)
    print(newstack)
    stacks.append(newstack)


# LOAD AND CLEAN DATA
def create_stacks():
    s1 = ['Q','F','L','S','R']
    s2 = ['T','P','G','Q','Z','N']
    s3 = ['B','Q','M','S']
    s4 = ['Q','B','C','H','J','Z','G','T']
    s5 = ['S','F','N','B','M','H','P']
    s6 = ['G','V','L','S','N','Q','C','P']
    s7 = ['F','C','W']
    s8 = ['M','P','V','W','Z','G','H','Q']
    s9 = ['R','N','C','L','D','Z','G']

    stacks = []
    stacks.append(s1)
    stacks.append(s2)
    stacks.append(s3)
    stacks.append(s4)
    stacks.append(s5)
    stacks.append(s6)
    stacks.append(s7)
    stacks.append(s8)
    stacks.append(s9)
    return stacks
stacks = create_stacks()


def move(qtd,wfrom,wto,stacks):
    #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
    for i in range(qtd):
        to_move = stacks[wfrom-1][0]
        stacks[wfrom-1].pop(0)
        stacks[wto-1].insert(0, to_move)

def move2(qtd,wfrom,wto,stacks):
    #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
    print(len(stacks[wto-1])+len(stacks[wfrom-1]))
    s_to_move = stacks[wfrom-1][0:qtd]
    #print(s_to_move)
    for i in range(qtd):
        to_move = s_to_move[-1]
        #print(to_move)
        s_to_move.pop(-1)
        #print(to_move)
        stacks[wfrom-1].pop(len(s_to_move))
        #print(stacks[wfrom-1])
        stacks[wto-1].insert(0, to_move)
    print(len(stacks[wto-1])+len(stacks[wfrom-1]))
    

def movex(qtd,wfrom,wto):
    #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
    for i in range(int(qtd)):
        if wfrom == 1:
            to_move = s1[0]
            s1.pop(0)
        if wfrom == 2:
            to_move = s2[0]
            s2.pop(0)
        if wfrom == 3:
            to_move = s3[0]
            s3.pop(0)
        if wfrom == 4:
            to_move = s4[0]
            s4.pop(0)
        if wfrom == 5:
            to_move = s5[0]
            s5.pop(0)
        if wfrom == 6:
            to_move = s6[0]
            s6.pop(0)
        if wfrom == 7:
            to_move = s7[0]
            s7.pop(0)
        if wfrom == 8:
            to_move = s8[0]
            s8.pop(0)
        if wfrom == 9:
            to_move = s9[0]
            s9.pop(0)
        if wto == 1:
            s1.insert(0, to_move)
        if wto == 2:
            s2.insert(0, to_move)
        if wto == 3:
            s3.insert(0, to_move)
        if wto == 4:
            s4.insert(0, to_move)
        if wto == 5:
            s5.insert(0, to_move)
        if wto == 6:
            s6.insert(0, to_move)
        if wto == 7:
            s7.insert(0, to_move)
        if wto == 8:
            s8.insert(0, to_move)
        if wto == 9:
            s9.insert(0, to_move)
    

#stacks = create_stacks()
for n in input_day5:
    values = n.split(' ')
    move(int(values[1]),int(values[3]),int(values[5]),stacks)

result = stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0]
print("Resultado da Primeira Parte: " + str(result))

stacks = create_stacks()
print(len(stacks[0]) + len(stacks[1])  + len(stacks[2]) +
len(stacks[2]) + len(stacks[4])  + len(stacks[5]) +
len(stacks[5]) + len(stacks[7])  + len(stacks[8]))
for n in input_day5:
    values = n.split(' ')
    #print("entrada:")
    #print(len(stacks[0]) + len(stacks[1])  + len(stacks[2]) +
    #len(stacks[2]) + len(stacks[4])  + len(stacks[5]) +
    #len(stacks[5]) + len(stacks[7])  + len(stacks[8]))

    move2(int(values[1]),int(values[3]),int(values[5]),stacks)

    #print("saida:")
    #print(len(stacks[0]) + len(stacks[1])  + len(stacks[2]) +
    #len(stacks[2]) + len(stacks[4])  + len(stacks[5]) +
    #len(stacks[5]) + len(stacks[7])  + len(stacks[8]))

result = stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0]
print("Resultado da Primeira Parte: " + str(result))

