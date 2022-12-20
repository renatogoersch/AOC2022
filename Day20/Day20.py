with open('ti.csv') as file:
    input = [line.rstrip() for line in file]

new_list = []


for n in range(len(input)):
    add = (int(input[n]),n)
    new_list.append(add)

new_list2 = new_list.copy()


def move_left(pos):
    for n in range(len(new_list)):
        if new_list2[n][1] == pos:
            new_pos = new_list2[n][1]-1
            if new_pos < 0:
                new_pos = 6
            new_list2[n] = (new_list2[n][0],new_pos)
            new_list2.sort(key=lambda tup: tup[1])
            for k in range(len(new_list)):
                if new_list2[n][1] == new_list2[k][1] and new_list2[k][1] :


def move_right(pos):
    for n in range(len(new_list)):
        #print(n,pos)
        if new_list2[n][1] == pos:
            new_pos = new_list2[n][1]+1
            if new_pos > 6:
                new_pos = 0
            new_list2[n] = (new_list2[n][0],new_pos)
            new_list2.sort(key=lambda tup: tup[1])



print(new_list2)
for n in range(len(new_list)):
    if new_list[n][0] < 0:
        print("moved left",new_list[n][0],new_list[n][1],"-",abs(new_list[n][0]),"times")
        for k in range(abs(new_list[n][0])):
            move_left(new_list[n][1])
    elif new_list[n][0] > 0:
        print("moved right",new_list[n][0],new_list[n][1],"-",abs(new_list[n][0]),"times")
        for k in range(abs(new_list[n][0])):
            move_left(new_list[n-1][1])
    else:
        print("no move",new_list[n][0])
    print(new_list2)