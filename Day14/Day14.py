with open('input_day14.csv') as file:
#with open('ti.csv') as file:
    input_day14 = [line.rstrip() for line in file]
import numpy as np

grid = [[' ' for c in range(700)] for r in range(700)]

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
            max_y = y_1
        if y_2 > max_y:
            max_y = y_2

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
        #print(n[492:512])
        print(n[492:560])
        cox+=1
        if cox>180:
            break

class Sand:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def moved(self, abyss):
        global grid, max_y, q
        if self.y-1 > max_y:
            print(self.y,self.x)
            q=None
            return
        #print(self.y,max_y)
        down = grid[self.y+1][self.x]
        down_left = grid[self.y+1][self.x-1]
        left = grid[self.y][self.x-1]
        down_right = grid[self.y+1][self.x+1]
        right = grid[self.y][self.x+1]
        if down == " ":
            grid[self.y][self.x] = ' '
            self.y += 1
            print("md", self.x, self.y)
            grid[self.y][self.x] = 'o'
            down = grid[self.y+1][self.x]
            self.moved(abyss)
        elif down == "o":
            self.movedl(abyss)
        elif down == "#" and left == ' ' and down_left == ' ':
            self.x -= 1
            self.y += 1
            grid[self.y-1][self.x+1] = ' '
            grid[self.y][self.x] = 'o'
            self.moved(abyss)
        elif down == "#" and right == ' ' and down_right == ' ':
            self.x += 1
            self.y += 1
            grid[self.y+1][self.x+1] = ' '
            grid[self.y][self.x] = 'o'
            self.moved(abyss)

    def movedl(self, abyss):
        global grid
        #left = grid[self.y][self.x-1]
        down_left = grid[self.y+1][self.x-1]
        left_left = grid[self.y][self.x-2]
        if down_left == " ":
            print("ml", self.x, self.y)
            self.x -= 1
            self.y += 1
            grid[self.y-1][self.x+1] = ' '
            grid[self.y][self.x] = 'o'
            res = self.path_right()
            if res == True:
                self.movedl(abyss)
            else:
                self.moved(abyss)
        else:
            self.movedr(abyss)

    def movedr(self, abyss):
        global grid
        right = grid[self.y][self.x+1]
        right_right = grid[self.y][self.x+2]
        down_right = grid[self.y+1][self.x+1]
        if down_right == " ":
            print("mr",self.x,self.y)
            self.x += 1
            self.y += 1
            grid[self.y-1][self.x-1] = ' '
            grid[self.y][self.x] = 'o'
            res = self.path_right()
            if res == True:
                self.movedr(abyss)
            else:
                self.moved(abyss)
    
    def path_right(self):
        global grid
        down_right = grid[self.y+1][self.x+1]
        down_down_right = grid[self.y+2][self.x+1]
        if down_right == " " and down_down_right == " ":
            return True
        else:
            return False
    
    def path_left(self):
        global grid
        down_left = grid[self.y+1][self.x-1]
        down_down_left = grid[self.y+2][self.x-1]
        if down_left == " " and down_down_left == " ":
            return True
        else:
            return False

def create_sand(abyss):
    global grid
    #printx()
    sand = Sand((500,0))
    sand.moved(abyss)


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

#for y in range(len(grid)):
    #for x in range(len(grid[y])):
        #if x == max_x+1 or x == min_x-1:
            #grid[y][x] = '#'

snows=0
q = True
while q!=None:
    snows+=1
    resultx = create_sand(abyss)
    print(snows-1)
    print(grid[500][1])