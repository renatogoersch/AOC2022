os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day5")

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
input1 = []
input2 = []
p1 = '0'
with open('inputa.csv') as file:
    for line in file:
        if p1 == '0':
            if '1' in line:
                p1 = '1'
            else:
                input1.insert(0, line)
        else:
            input2.insert(0, line.rstrip())
input1 = Reverse(input1)
input2 = Reverse(input2)

def create_stacks():
    stacks = []
    for i in range(int(len(input1[0])/4)):
        newstack = []
        for n in range(len(input1)):
            letter = input1[n][1+(4*i)]
            newstack.insert(0, letter)
        while ' ' in newstack:
            newstack.remove(' ')
        #stacks.append(newstack)
        stacks.append(list(reversed(newstack)))
    return stacks

stacks = create_stacks()

def move(qtd,wfrom,wto,stacks,version):
    if version == 1:
        #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
        for i in range(qtd):
            to_move = stacks[wfrom-1][0]
            stacks[wfrom-1].pop(0)
            stacks[wto-1].insert(0, to_move)
    elif version == 2:
    #print("Transferir " + str(qtd) + " de " + str(wfrom) + " para " + str(wto))
        s_to_move = stacks[wfrom-1][0:qtd]
        for i in range(qtd):
            to_move = s_to_move[-1]
            s_to_move.pop(-1)
            stacks[wfrom-1].pop(len(s_to_move))
            stacks[wto-1].insert(0, to_move)


stacks = create_stacks()
for n in input2:
    values = n.split(' ')
    move(int(values[1]),int(values[3]),int(values[5]),stacks,1)

result = stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0]
print("Resultado da Primeira Parte: " + str(result))
    
stacks = create_stacks()
for n in input2:
    values = n.split(' ')
    move(int(values[1]),int(values[3]),int(values[5]),stacks,2)

result = stacks[0][0] + stacks[1][0] + stacks[2][0] + stacks[3][0] + stacks[4][0] + stacks[5][0] + stacks[6][0] + stacks[7][0] + stacks[8][0]
print("Resultado da Segunda Parte: " + str(result))
