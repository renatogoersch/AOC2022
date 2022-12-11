os.chdir(r"C:\Users\renat\Documents\AOC2022\AOC2022\Day11")
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

with open('input_day11.csv') as file:
#with open('ti.csv') as file:
    input_day11 = [line.rstrip() for line in file]

import time

items = []

class Item:
    def __init__(self, owner):
        self.owner = owner
        self.name = len(items)+1

class Monkeys:
    def __init__(self, position,start,monkey_operation,
        monkey_test,monkey_if1,monkey_if2):
        self.name = position
        self.items = list(map(int, start))
        self.operation = monkey_operation
        self.test = (str(monkey_test[0]),int(monkey_test[1]))
        self.if1 = int(monkey_if1)
        self.if2 = int(monkey_if2)
        self.inspected = int(0)

    def inspect(self):
        items = self.items.copy()
        for i in items:
            self.inspected += 1
            worry = int(i)
            if self.operation[1] == 'old':
                worry = ops[self.operation[0]](worry,worry)
            else:
                worry = ops[self.operation[0]](worry,
                    int(self.operation[1]))
            worry = int(worry/3)
            if (worry % self.test[1]) > 0:
                monkeys[self.if2].throw(worry)
            else:
                monkeys[self.if1].throw(worry)
        self.items = []

    def inspect2(self,worry):
        items = self.items.copy()
        for worry in items:
            self.inspected += 1
            nworry = worry
            nworry %= mod
            if self.operation[1] == 'old':
                nworry = ops[self.operation[0]](nworry,nworry)
            else:
                nworry = ops[self.operation[0]](nworry,
                    int(self.operation[1]))
            if (nworry % self.test[1]) == 0:
                monkeys[self.if1].throw(nworry)
            else:
                monkeys[self.if2].throw(nworry)
        self.items = []
    def throw(self,item):
        self.items.append(item)


def create_monkeys(monkeys,nmonkeys):
    for m in range(nmonkeys):
        start = input_day11[1+(7*m)].split(': ')[1].split(', ')
        monkey_operation = (input_day11[2+(7*m)].split(' ')[6],
        input_day11[2+(7*m)].split(' ')[7])
        monkey_test = (input_day11[3+(7*m)].split(' ')[3],
        input_day11[3+(7*m)].split(' ')[5])
        monkey_if1 = input_day11[4+(7*m)].split(' ')[9]
        monkey_if2 = input_day11[5+(7*m)].split(' ')[9]
        monkey = Monkeys(m,start,monkey_operation,monkey_test,
            monkey_if1,monkey_if2)
        monkeys.append(monkey)
    return monkeys

nmonkeys = 8
monkeys = []
monkeys = create_monkeys(monkeys,nmonkeys)
        
    
def hunt_monkeys(monkeys,nmonkeys):
    for r in range(nmonkeys):
        monkeys[r].inspect()

rounds = 20
for n in range(rounds):
    hunt_monkeys(monkeys,nmonkeys)


monkeys.sort(key=lambda x: x.inspected, reverse=True)
print(monkeys[0].inspected * monkeys[1].inspected)

nmonkeys = 8
monkeys = []
monkeys = create_monkeys(monkeys,nmonkeys)
        
mod = 1
for monkey in monkeys:
    mod *= int(monkey.test[1])
worry = 0
def hunt_monkeys(monkeys,nmonkeys,worry):
    for r in range(nmonkeys):
        worry = monkeys[r].inspect2(worry)

rounds = 10000
for n in range(rounds):
    hunt_monkeys(monkeys,nmonkeys,worry)

monkeys.sort(key=lambda x: x.inspected, reverse=True)
print(monkeys[0].inspected * monkeys[1].inspected)