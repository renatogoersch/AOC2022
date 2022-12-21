"""

Rocks
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

"""
from operator import attrgetter

with open('day17_input.csv') as file:
#with open('ti.csv') as file:
    jets = [line.rstrip() for line in file]

import numpy as np
clean = '.'
blocks = []
blocks.append('#')
blocks.append('_')
blocks.append('|')
maxy=3500
grid = [[clean for c in range(9)] for r in range(maxy)]
born = maxy-5
for n in range(len(grid)):
    grid[n][0] = '|'
    grid[n][8] = '|'

steps = [0 for c in range(maxy)]
for x in range(1,len(grid[maxy-1])-1):
    grid[maxy-1][x] = blocks[1]

all_rocks = []
class rocks:
    def __init__(self, location):
        self.location = location
        self.loc_y = maxy
        #print(location[0],location[1])
        grid[location[0]][location[1]] = '@'
        all_rocks.append(self)

    def move(self):
        #print(self.location)
        #print(grid[self.location[0]][self.location[1]])
        #print(block)
        if grid[self.location[0]+1][self.location[1]] in blocks:
            pass
            #print("bump function not working")
        else:
            grid[self.location[0]][self.location[1]] = '.'
            grid[self.location[0]+1][self.location[1]] = '@'
            self.location = (self.location[0]+1,self.location[1])

    def move_left(self):
        if grid[self.location[0]][self.location[1]-1] in blocks:
            pass
        else:
            grid[self.location[0]][self.location[1]] = '.'
            grid[self.location[0]][self.location[1]-1] = '@'
            self.location = (self.location[0],self.location[1]-1)
            
    def move_right(self):
        if grid[self.location[0]][self.location[1]+1] in blocks:
            pass
        else:
            grid[self.location[0]][self.location[1]] = '.'
            grid[self.location[0]][self.location[1]+1] = '@'
            self.location = (self.location[0],self.location[1]+1)
            
            

class _:
    def __init__(self) -> None:
        self.rocks = list()
        self.rocks += [rocks((born,3))]
        self.rocks += [rocks((born,4))]
        self.rocks += [rocks((born,5))]
        self.rocks += [rocks((born,6))]
        self.rocks.reverse()
        self.bumped = 0

    def move(self):
        for r in self.rocks:
            #print(grid[r.location[0]+1][r.location[1]])
            if self.bump(grid[r.location[0]+1][r.location[1]]) == True:
                self.bumped = 1
                self.Bumped()
                #print("bump",r)
                return 'Bump'
        for r in self.rocks:
            #print("move",r)
            r.move()

    def bump(self,rock):
        if rock in blocks:
            return True
        
    def Bumped(self):
        global born
        for rock in self.rocks:
            grid[rock.location[0]][rock.location[1]] = "#"
            rock.loc_y = rock.location[0]
        born = min(all_rocks, key=attrgetter('loc_y')).loc_y-4
        global drop
        global steps
        loc = min(self.rocks, key=attrgetter('loc_y')).loc_y
        if steps[loc] == 0:
            steps[loc] = drop



    def jet(self,side):
        if side == '>':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]+1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_right()
        if side == '<':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]-1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_left()
            
            
class X:
    def __init__(self) -> None:
        self.rocks = []
        self.rocks += [rocks((born-2,4))]
        self.rocks += [rocks((born-1,3))]
        self.rocks += [rocks((born-1,4))]
        self.rocks += [rocks((born-1,5))]
        self.rocks += [rocks((born,4))]
        self.rocks.reverse()
        self.bumped = 0

    def move(self):
        for r in self.rocks:
            #print(grid[r.location[0]+1][r.location[1]])
            if self.bump(grid[r.location[0]+1][r.location[1]]) == True:
                self.bumped = 1
                self.Bumped()
                #print("bump",r)
                return 'Bump'
        for r in self.rocks:
            #print("move",r)
            r.move()
        
    def bump(self,rock):
        if rock in blocks:
            return True
        
    def Bumped(self):
        global born
        for rock in self.rocks:
            grid[rock.location[0]][rock.location[1]] = "#"
            rock.loc_y = rock.location[0]
        born = min(all_rocks, key=attrgetter('loc_y')).loc_y-4
        global drop
        global steps
        loc = min(self.rocks, key=attrgetter('loc_y')).loc_y
        if steps[loc] == 0:
            steps[loc] = drop



    def jet(self,side):
        if side == '>':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]+1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_right()
        if side == '<':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]-1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_left()


class L:
    def __init__(self) -> None:
        self.rocks = []
        self.rocks += [rocks((born-2,5))]
        self.rocks += [rocks((born-1,5))]
        self.rocks += [rocks((born,5))]
        self.rocks += [rocks((born,4))]
        self.rocks += [rocks((born,3))]
        self.rocks.reverse()
        self.bumped = 0

    def move(self):
        for r in self.rocks:
            #print(grid[r.location[0]+1][r.location[1]])
            if self.bump(grid[r.location[0]+1][r.location[1]]) == True:
                self.bumped = 1
                self.Bumped()
                #print("bump",r)
                return 'Bump'
        for r in self.rocks:
            #print("move",r)
            r.move()
        
    def bump(self,rock):
        if rock in blocks:
            return True
        
    def Bumped(self):
        global born
        for rock in self.rocks:
            grid[rock.location[0]][rock.location[1]] = "#"
            rock.loc_y = rock.location[0]
        born = min(all_rocks, key=attrgetter('loc_y')).loc_y-4
        global drop
        global steps
        loc = min(self.rocks, key=attrgetter('loc_y')).loc_y
        if steps[loc] == 0:
            steps[loc] = drop




    def jet(self,side):
        if side == '>':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]+1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_right()
        if side == '<':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]-1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_left()

class I:
    def __init__(self) -> None:
        self.rocks = []
        #print("I",born)
        self.rocks += [rocks((born-3,3))]
        self.rocks += [rocks((born-2,3))]
        self.rocks += [rocks((born-1,3))]
        self.rocks += [rocks((born,3))]
        self.rocks.reverse()
        self.bumped = 0

    def move(self):
        global born
        for r in self.rocks:
            #print(grid[r.location[0]+1][r.location[1]])
            if self.bump(grid[r.location[0]+1][r.location[1]]) == True:
                self.bumped = 1
                self.Bumped()
                #print("bump",r)
                return 'Bump'
        for r in self.rocks:
            #print("move",r)
            r.move()

    def bump(self,rock):
        if rock in blocks:
            return True
        
    def Bumped(self):
        global born
        for rock in self.rocks:
            grid[rock.location[0]][rock.location[1]] = "#"
            rock.loc_y = rock.location[0]
        born = min(all_rocks, key=attrgetter('loc_y')).loc_y-4
        global drop
        global steps
        loc = min(self.rocks, key=attrgetter('loc_y')).loc_y
        if steps[loc] == 0:
            steps[loc] = drop


    def jet(self,side):
        if side == '>':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]+1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_right()
        if side == '<':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]-1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_left()


class square:
    def __init__(self) -> None:
        self.rocks = []
        self.rocks += [rocks((born-1,3))]
        self.rocks += [rocks((born-1,4))]
        self.rocks += [rocks((born,3))]
        self.rocks += [rocks((born,4))]
        self.rocks.reverse()
        self.bumped = 0

    def move(self):
        for r in self.rocks:
            #print(grid[r.location[0]+1][r.location[1]])
            if self.bump(grid[r.location[0]+1][r.location[1]]) == True:
                self.bumped = 1
                self.Bumped()
                #print("bump",r)
                return 'Bump'
        for r in self.rocks:
            #print("move",r)
            r.move()
        
    def bump(self,rock):
        if rock in blocks:
            return True
        
    def Bumped(self):
        global born
        for rock in self.rocks:
            grid[rock.location[0]][rock.location[1]] = "#"
            rock.loc_y = rock.location[0]
        born = min(all_rocks, key=attrgetter('loc_y')).loc_y-4
        global drop
        global steps
        loc = min(self.rocks, key=attrgetter('loc_y')).loc_y
        if steps[loc] == 0:
            steps[loc] = drop


    def jet(self,side):
        if side == '>':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]+1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_right()
        if side == '<':
            for r in self.rocks:
                if self.bump(grid[r.location[0]][r.location[1]-1]) == True:
                    return 'Bump'
            for r in self.rocks:
                r.move_left()

import time
start_time = time.time()

def printx(y,r,rr):
    range1 = y
    range2 = maxy
    if range1 < 0:
        range1 = 0 
    if range2 > maxy:
        range2 = maxy
    for yy in range(range1,range2):
        #print(yy)
        print(yy,grid[yy])
    print("-----------------------------------------------")

def next_rock(next_drop):
    if next_drop == '_':
        return _(),'x'
    if next_drop == 'x':
        return X(),'L'
    if next_drop == 'L':
        return L(),'I'
    if next_drop == 'I':
        return I(),'square'
    if next_drop == 'square':
        return square(),'_'
    
drop = 0
next_drop = '_'


def refill_jet(to_jet):
    for n in jets[0]:
        to_jet.append(n)
    return to_jet
    
to_jet = []
to_jet = refill_jet(to_jet)


tall = []
old_drop = 0
while drop < 2022:
    drop += 1
    #print("drop",next_drop)
    rock,next_drop = next_rock(next_drop)
    #printx(rock.rocks[0].location[0],10000)
    while rock.bumped == 0:
        if(rock.bumped == 0):
            #print(to_jet[0])
            rock.jet(to_jet[0])
            #print("jet to",to_jet[0])
            to_jet.pop(0)
            if len(to_jet) == 0:
                to_jet = refill_jet(to_jet)
        rock.move()
    for i in range(len(grid)):
        if '#' in grid[i]:
            tally = maxy-i
            break
    tall.append((drop,tally,tally/drop))
    #printx(born,5,10)
    #print(drop,"-------------- move ---------------")


for i in range(len(grid)):
    if '#' in grid[i]:
        print(maxy-i-1)
        break

old_n = 0
when = 0
pat = []
for n in range(4,len(grid)):
    if grid[n-1] == grid[maxy-2]:
        if grid[n-2] == grid[maxy-3]:
            if grid[n-3] == grid[maxy-4]:
                if grid[n-4] == grid[maxy-5]:
                    if grid[n-5] == grid[maxy-6]:
                        #print(n,old_n)
                        pat.append((n,n-old_n))
                        old_n = n

pat.reverse()
grid2 = grid
grid2 = [n for n in grid if n != grid[2]]

#total = 1000000000000

#first_steps = tall[pat[0]][1]
#p1 = (tall[pat[1]+pat[1]][1] - tall[pat[1]][1])

##p2 = ((total - first_steps) // pat[1])

#loops_steps = p1 * p2

##final_steps = tall[(total - first_steps) % pat[1]][1]

#print(first_steps + loops_steps + final_steps)


print("--- %s seconds ---" % (time.time() - start_time))