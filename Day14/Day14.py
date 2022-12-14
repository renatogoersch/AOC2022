#with open('input_day14.csv') as file:
with open('ti.csv') as file:
    input_day14 = [line.rstrip() for line in file]
import numpy as np

grid = [['.' for c in range(700)] for r in range(700)]

last_rock = 'None'

def create_rocks(rock_loc,grid):
    n = len(rock_loc)
    for _ in range(n-1):
        x_1 = int(rock_loc[0].split(',')[0])
        y_1 = int(rock_loc[0].split(',')[1])
        x_2 = int(rock_loc[1].split(',')[0])
        y_2 = int(rock_loc[1].split(',')[1])
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


for n in range(len(input_day14)):
    rock_loc = input_day14[n].split(' -> ')
    grid = create_rocks(rock_loc, grid)


def printx(grid):
    cox = 0
    for n in grid:
        print(n[493:505])
        cox+=1
        if cox>9:
            break

class Sand:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def moved(self, grid, abyss):
        down = grid[self.y+1][self.x]
        while down == ".":
            if (self.y+1) >= abyss:
                print("ABYSS")
                return 'ABYSS'
            grid[self.y][self.x] = '.'
            self.y += 1
            #print("md", self.x, self.y)
            grid[self.y][self.x] = 'o'
            down = grid[self.y+1][self.x]
        if down == "o":
            self.movedl(grid, abyss)

    def movedl(self, grid, abyss):
        left = grid[self.y][self.x-1]
        down_left = grid[self.y+1][self.x-1]
        if left == "." and down_left == ".":
            #print("ml", self.x, self.y)
            self.x -= 1
            grid[self.y][self.x+1] = '.'
            grid[self.y][self.x] = 'o'
            self.moved(grid, abyss)
        else:
            self.movedr(grid, abyss)

    def movedr(self, grid, abyss):
        right = grid[self.y][self.x+1]
        down_right = grid[self.y+1][self.x+1]
        if right == "." and down_right == ".":
            #print("mr",self.x,self.y)
            self.x += 1
            grid[self.y][self.x-1] = '.'
            grid[self.y][self.x] = 'o'
            self.moved(grid,abyss)



def create_sand(grid,abyss):
    printx(grid)
    sand = Sand((500,0))
    sand.moved(grid,abyss)


for n in range(len(grid)):
    count = 0
    for x in grid[-n]:
        if x == '#':
            count+=1
    if count > 0:
        print("Result", str(-n))
        abyss = -n
        break
abyss=abyss+701


snows = 0
q = True
while q!=None:
    resultx = create_sand(grid,abyss)
    snows+=1
    print(snows,resultx)
    if snows > 25:
        q=None