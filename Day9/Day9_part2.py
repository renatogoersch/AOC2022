os.chdir(r"C:\Users\renat\Documents\AOC2022\AOC2022\Day9")

with open('input_day9.csv') as file:
    input_day9 = [line.rstrip() for line in file]
    
rope = [['0']*1000]*1000
head_x = [499]*10
head_y = [499]*10

def move_head(tail_positions,direction,times,head_x,head_y):
    for _ in range(times):
        if direction == "R":
            head_x[0] = head_x[0] + 1
        elif direction == "D":
            head_y[0] = head_y[0] + 1
        elif direction == "L":
            head_x[0] = head_x[0] - 1
        else:
            head_y[0] = head_y[0] - 1
        head_x,head_y,tail_positions = move_tail(rope,head_x,head_y,tail_positions)
    return tail_positions,head_x,head_y


def move_tail(rope,head_x,head_y,tail_positions):
    for k in range(1,10):
        dist_x = head_x[k-1] - head_x[k]
        dist_y = head_y[k-1] - head_y[k]
        if (abs(dist_x) > 1 and abs(dist_y) > 1) or (abs(dist_x) > 1 and abs(dist_y) == 1) or (abs(dist_x) == 1 and abs(dist_y) > 1):
            if dist_x > 0 and dist_y > 0:
                head_x[k],head_y[k] = head_x[k]+1,head_y[k]+1
            elif dist_x > 0 and dist_y < 0:
                head_x[k],head_y[k] = head_x[k]+1,head_y[k]-1
            elif dist_x < 0 and dist_y > 0:
                head_x[k],head_y[k] = head_x[k]-1,head_y[k]+1
            elif dist_x < 0 and dist_y < 0:
                head_x[k],head_y[k] = head_x[k]-1,head_y[k]-1
        else:
            if dist_x == 2:
                head_x[k] = head_x[k]+1
            elif dist_x == -2:
                head_x[k] = head_x[k]-1
            elif dist_y == 2:
                head_y[k] = head_y[k]+1
            elif dist_y == -2:
                head_y[k] = head_y[k]-1
        if k == 9:
            tail_positions.append(str(head_x[k]) + ',' + str(head_y[k]))
        dist_x = head_x[k-1] - head_x[k]
        dist_y = head_y[k-1] - head_y[k]
    return head_x,head_y,tail_positions


tail_positions = list()
for n in range(len(input_day9)):
    direction = str(input_day9[n].split(" ")[0])
    times = int(input_day9[n].split(" ")[1])
    tail_positions,head_x,head_y = move_head(tail_positions,direction,times,
        head_x,head_y)
    
tail_positions = list(set(tail_positions))
print(len(tail_positions))