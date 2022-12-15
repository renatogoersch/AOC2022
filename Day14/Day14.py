with open('input_day14.csv') as file:
#with open('ti.csv') as file:
    input_day14 = [line.rstrip() for line in file]
import numpy as np

grid = [[' ' for c in range(1000)] for r in range(700)]

max_x = 500
min_x = 500
max_y = 0

def create_rocks(rock_loc):
    global grid
    n = len(rock_loc)
    for _ in range(n-1):
        x_1 = int(rock_loc[0].split(',')[0])
        y_1 = int(rock_loc[0].split(',')[1])
        x_2 = int(rock_loc[1].split(',')[0])
        y_2 = int(rock_loc[1].split(',')[1])

        global max_x,min_x,max_y
        if x_2 > max_x:
            max_x = x_2
        if x_1 > max_x:
            max_x = x_1
        if x_2 < min_x:
            min_x = x_2
        if x_1 < min_x:
            min_x = x_1

        if y_1 > max_y:
            #part1 max_y = y_1
            max_y = y_1 + 2
        if y_2 > max_y:
            #part1 max_y = y_1
            max_y = y_2 + 2

        if x_1 == x_2:
            if (y_2 > y_1):
                for y in range(y_1,(y_2+1)):
                    grid[y][x_1] = "#"
            elif (y_1 > y_2):
                for y in range(y_2,(y_1+1)):
                    grid[y][x_1] = "#"
            else:
                grid[x_1][y_1]  = "#"
        if y_1 == y_2:
            if (x_2 > x_1):
                for x in range(x_1,(x_2+1)):
                    grid[y_1][x] = "#"
            elif (x_1 > x_2):
                for x in range(x_2,(x_1+1)):
                    grid[y_1][x] = "#"
            else:
                grid[y_1][x_1]  = "#"
        rock_loc.pop(0)
    return grid



def printx():
    global grid
    cox = 0
    for n in grid:
        print(n[489:512])
        #print(n[120:190])
        cox+=1
        if cox>15:
            break

class Sand:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def moved(self):
        global grid, max_y, q
        if self.y-1 > max_y:
            print(self.y,self.x)
            q=None
            return
        down = grid[self.y+1][self.x]
        down_left = grid[self.y+1][self.x-1]
        left = grid[self.y][self.x-1]
        down_right = grid[self.y+1][self.x+1]
        right = grid[self.y][self.x+1]
        if down == " ":
            grid[self.y][self.x] = ' '
            self.y+=1
            grid[self.y][self.x] = 'o'
            self.moved()
        elif down_left == " ":
            grid[self.y][self.x] = ' '
            self.x-=1
            self.y+=1
            grid[self.y][self.x] = 'o'
            self.moved()
        elif down_right == " ":
            grid[self.y][self.x] = ' '
            self.x+=1
            self.y+=1
            grid[self.y][self.x] = 'o'
            self.moved()

        
        
def create_sand():
    global grid
    printx()
    sand = Sand((500,0))
    sand.moved()


for n in range(len(input_day14)):
    rock_loc = input_day14[n].split(' -> ')
    create_rocks(rock_loc)

snows = 0
for n in range(len(grid)):
    count = 0
    count2 = 0
    for x in grid[-n]:
        if x == '#':
            count+=1
        else:
            count2+=1
    if count > 0:
        if count2 > 0:
            #print("Result", str(n), count2)
            abyss = (n,count2)
            break

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if x == 500-max_y:
            grid[y][x] = '#'
        if x == 500+max_y:
            grid[y][x] = '#'
        if y == max_y:
            grid[y][x] = '#'

snows=0
q = True
while q!=None:
    end_left = grid[max_y-1][500-max_y+1]
    end_right = grid[max_y-1][500+max_y-1]
    left = grid[max_y-1][500-max_y+1]

    down = grid[1][499]
    down_left = grid[1][500]
    down_right = grid[1][501]
    if end_left == 'o' and end_right == 'o' and down == 'o' and down_left == 'o' and down_right == 'o':
        print("FINISH")
        grid[0][500] = 'o'
        q=None
    snows+=1
    resultx = create_sand()
    #if snows > 100:
        #q = None
    print(snows)
    print(grid[500][1])