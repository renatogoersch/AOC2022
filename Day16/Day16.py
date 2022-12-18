from operator import attrgetter
 
#with open('input_day16.csv') as file:
with open('ti.csv') as file:
    input_day16 = [line.rstrip() for line in file]


class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to

    def update_lead_to(self, valves):
        lead_to = []
        for valve in self.lead_to:
            obj = next(v for v in valves if str(v.name) == str(valve))
            lead_to.append(obj)
        self.lead_to = lead_to


class Person:
    def __init__(self, m_pr, where, next_move):
        self.where = where
        self.next_move = next_move
        self.m_pr = m_pr
        self.Time = 30
        self.opened_valves = []

    def move(self):
        if self.Time <= 0:
            return
        #print("Move from", str(self.where),"to", str(self.next_move))
        self.Time -= 1
        obj = next(v for v in valves if str(v.name) == self.next_move)
        self.where = obj.name
        #print(1,self.where,self.opened_valves)
        if self.where not in self.opened_valves:
            #print(2,self.where,self.opened_valves)
            self.m_pr += obj.flow_rate
            self.opened_valves.append(obj.name)
        for n in obj.lead_to:
            print(self.where,n.name)
        self.next_move = max(obj.lead_to, key=attrgetter('flow_rate')).name
        self.Time -= 1
        #print("Opened", str(self.where),"max_pr",self.m_pr)
        self.move()


valves = []
for row in input_day16:
    name = row.split(';')[0].split(' ')[1]
    flow_rate = int(row.split(';')[0].split(' ')[4].split('=')[1])
    if 'valves' in row.split(' '):
        lead_to = row.split(';')[1].split('valves ')[1].split(', ')
    else:
        lead_to = row.split(';')[1].split('valve ')[1].split(', ')
    valves.append(Valve(name, flow_rate, lead_to))

for v in valves:
    v.update_lead_to(valves)

m_pr = 0
person = Person(m_pr, '', valves[0].name)
while person.Time > 0:
    person.move()

grid = [['' for c in valves] for r in valves]
INF = 1000
n = 0
for v1 in valves:
    i = 0  
    for v2 in valves:
        if v1 == v2:
            grid[n][i] = int(0)
        elif v2 in v1.lead_to:
            grid[n][i] = int(v1.flow_rate)
        else:
            grid[n][i] = INF
        i+=1
    n+=1
#print(grid)
nV = 10

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

floyd_warshall(grid)
