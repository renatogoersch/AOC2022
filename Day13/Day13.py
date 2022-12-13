with open('input_day13.csv') as file:
#with open('ti.csv') as file:
    input_day13 = [line.rstrip() for line in file]

size = int((len(input_day13) - 1)/3)

comp_list = []
for n in range(size+1):
    value = [ast.literal_eval(input_day13[(3*n)]),
    ast.literal_eval(input_day13[1+(3*n)])]
    comp_list.append(value)


def compare(l1,l2):
    if type(l1) == int and type(l2) == int:
        if l1 < l2:
            return 1
        elif l1 == l2:
            return 0
        else:
            return -1
    elif type(l1) == list and type(l2) == list:
        i = 0
        while i<len(l1) and i<len(l2):
            comp = compare(l1[i], l2[i])
            if comp==1:
                return 1
            if comp==-1:
                return -1
            i += 1
        if i==len(l1) and i<len(l2):
            return 1
        elif i==len(l2) and i<len(l1):
            return -1
        else:
            return 0
    if type(l1) == int and type(l2) == list:
        return compare([l1], l2)
    else:
        return compare(l1, [l2])

packets = []
parte1=0
index=0
for l in comp_list:
    index+=1
    comp = compare(l[0],l[1])
    if comp == 1:
        parte1 += index
    packets.append([l[0]])
    packets.append([l[1]])
print(parte1)
packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key
packets = sorted(packets, key=cmp_to_key(lambda p1,p2: compare(p1,p2)), reverse=True)
parte2 = 1
for i,p in enumerate(packets):
    if p==[[2]] or p==[[6]]:
        parte2 *= i+1
print(parte2)