os.chdir(r"C:\Users\renat\Documents\AOC2022\AOC2022\Day9")

with open('input_day9.csv') as file:
    input_day9 = [line.rstrip() for line in file]
rope = [['0']*1000]*1000
head_x = 499
head_y = 499
tail_x = 499
tail_y = 499

def move_head(tail_positions,direction,times,rope,head_x,head_y,tail_x,tail_y,count):
    print(direction,str(times))
    for _ in range(times):
        if direction == "R":
            head_x = head_x + 1
        elif direction == "D":
            head_y = head_y + 1
        elif direction == "L":
            head_x = head_x - 1
        else:
            head_y = head_y - 1
        count,rope,head_x,head_y,tail_x,tail_y,tail_positions = move_tail(rope,head_x,head_y,tail_x,tail_y,count,tail_positions)
    return tail_positions,rope,head_x,head_y,tail_x,tail_y,count


def move_tail(rope,head_x,head_y,tail_x,tail_y,count,tail_positions):
    dist_x = head_x - tail_x
    dist_y = head_y - tail_y
    print(dist_x, dist_y)
    if (abs(dist_x) > 1 and abs(dist_y) > 1) or (abs(dist_x) > 1 and abs(dist_y) == 1) or (abs(dist_x) == 1 and abs(dist_y) > 1):
        if dist_x > 0 and dist_y > 0:
            print("move x1")
            tail_x,tail_y = tail_x+1,tail_y+1
        elif dist_x > 0 and dist_y < 0:
            print("move x2")
            tail_x,tail_y = tail_x+1,tail_y-1
        elif dist_x < 0 and dist_y > 0:
            print("move x3")
            tail_x,tail_y = tail_x-1,tail_y+1
        elif dist_x < 0 and dist_y < 0:
            print("move x4")
            tail_x,tail_y = tail_x-1,tail_y-1
    else:
        if dist_x == 2:
            tail_x = tail_x+1
            print("move x5")
        elif dist_x == -2:
            tail_x = tail_x-1
            print("move x6")
        elif dist_y == 2:
            tail_y = tail_y+1
            print("move x7")
        elif dist_y == -2:
            tail_y = tail_y-1
            print("move x8")
    tail_positions.append(str(tail_x) + ',' + str(tail_y))
    dist_x = head_x - tail_x
    dist_y = head_y - tail_y
    print("==========")
    return count,rope,head_x,head_y,tail_x,tail_y,tail_positions


rope[head_x][head_y] = "S"
count=0
tail_positions = list()
for n in range(len(input_day9)):
    direction = str(input_day9[n].split(" ")[0])
    times = int(input_day9[n].split(" ")[1])
    ##print("move to " + direction + " " + str(times) + " vezes")
    tail_positions,rope,head_x,head_y,tail_x,tail_y,count = move_head(tail_positions,direction,times,rope,
        head_x,head_y,tail_x,tail_y,count)
    
tail_positions = list(set(tail_positions))
#print(count)