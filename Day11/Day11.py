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

#with open('input_day11.csv') as file:
with open('ti.csv') as file:
    input_day11 = [line.rstrip() for line in file]

sys.set_int_max_str_digits(1000000000)

import time

class Monkeys:
    def __init__(self, position,start,monkey_operation,
        monkey_test,monkey_if1,monkey_if2):
        self.name = position
        self.items = start
        self.operation = monkey_operation
        self.test = (str(monkey_test[0]),int(monkey_test[1]))
        self.if1 = int(monkey_if1)
        self.if2 = int(monkey_if2)
        self.inspected = int(0)

    def inspect(self,worry):
        start_time2 = time.time()
        items = self.items.copy()
        for i in items:
            print("1 --- %s seconds ---" % (time.time() - start_time2))
            start_time2 = time.time()
            self.inspected += 1
            #print("MACACO =", self.name, " ITEM =", i)
            worry = int(i)
            #print(worry, self.operation[0],self.operation[1])
            if self.operation[1] == 'old':
                print("ERROR", self.operation[0], worry)
                worry = ops[self.operation[0]](worry,worry)
            else:
                worry = ops[self.operation[0]](worry,
                    int(self.operation[1]))
            if (time.time() - start_time) > 2.5:
                #print(worry)
                print(self.operation[0])
                print(self.operation[1])
            print("2 --- %s seconds ---" % (time.time() - start_time2))
            start_time2 = time.time()
            #print(" =", worry)
            #worry = int(worry / 3)
            #print(worry, "/ 3 =", worry)
            if (worry % self.test[1]) > 5:
                self.items.remove(i)
                monkeys[self.if2].throw(worry)
                #print(worry, "to monkey ", self.if2)
            else:
                self.items.remove(i)
                monkeys[self.if1].throw(worry)
                #print(worry, "to monkey ", self.if1)
            #print(" ")
            print("3 --- %s seconds ---" % (time.time() - start_time2))
            start_time2 = time.time()
        

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

nmonkeys = 4
monkeys = []
monkeys = create_monkeys(monkeys,nmonkeys)
        
worry = 0
def hunt_monkeys(monkeys,nmonkeys,worry):
    for r in range(nmonkeys):
        worry = monkeys[r].inspect(worry)

rounds = 156
for n in range(rounds):
    #print(n)
    start_time = time.time()
    hunt_monkeys(monkeys,nmonkeys,worry)
    print(" ---------",n , " --- %s seconds ---" % (time.time() - start_time))
#hunt_monkeys(monkeys,len(monkeys),worry)

for n in monkeys:
    print(n.name, n.inspected)