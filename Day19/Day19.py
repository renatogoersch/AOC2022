with open('input_day19.csv') as file:
#with open('ti.csv') as file:
    input = [line.rstrip() for line in file]

class ore_robot_recipe:
    def __init__(self,ore):
        self.ore = ore

class clay_robot_recipe:
    def __init__(self,ore):
        self.ore = ore

class obisidian_robot_recipe:
    def __init__(self,ore,clay):
        self.ore = ore
        self.clay = clay

class geode_robot_recipe:
    def __init__(self,ore,obs):
        self.ore = ore
        self.obs = obs

class Blueprint:
    def __init__(self,blueprint,ore_robot,clay_robot,obsidian_robot_rO,
        obsidian_robot_rC,geode_robot_rO,geode_robot_rOB):
            self.bp = blueprint
            self.minutes = 24
            orr = ore_robot_recipe(ore_robot)
            crr = clay_robot_recipe(clay_robot)
            obrr = obisidian_robot_recipe(obsidian_robot_rO,obsidian_robot_rC)
            grr = geode_robot_recipe(geode_robot_rO,geode_robot_rOB)
            self.recipe_orr = orr
            self.recipe_crr = crr
            self.recipe_obrr = obrr
            self.recipe_grr = grr
            
            self.robot_ore = 1
            self.robot_clay = 0
            self.robot_obs = 0
            self.robot_geode = 0

            self.ore = 0
            self.clay = 0
            self.obs = 0
            self.geode = 0
            self.max_geode = []

            print("Created a Blueprint number",self.bp)

    def collect(self):
        self.ore += 1*self.robot_ore
        self.clay += 1*self.robot_clay
        self.obs += 1*self.robot_obs
        self.geode += 1*self.robot_geode

    def upgrade_geode(self):
        if self.ore > self.recipe_grr.ore and self.obs > self.recipe_grr.obs:
            self.ore -= self.recipe_grr.ore
            self.obs -= self.recipe_grr.obs
            self.robot_geode += 1

    def upgrade_obs(self):
        if self.ore > self.recipe_obrr.ore and self.clay > self.recipe_obrr.clay:
            self.ore -= self.recipe_obrr.ore
            self.clay -= self.recipe_obrr.clay
            self.robot_obs += 1
        
    def upgrade_clay(self):
        if self.ore > self.recipe_obrr.ore:
            self.ore -= self.recipe_obrr.ore
            self.robot_clay += 1

    def upgrade_ore(self):
        if self.ore > self.recipe_obrr.ore:
            self.ore -= self.recipe_obrr.ore
            self.robot_ore += 1

    def reset(self):
        self.robot_ore = 1
        self.robot_clay = 0
        self.robot_obs = 0
        self.robot_geode = 0

        self.ore = 0
        self.clay = 0
        self.obs = 0
        self.geode = 0
        
    def simulate(self):
        self.upgrade_geode()
        self.upgrade_obs()
        self.upgrade_clay()
        self.upgrade_ore()




        self.minutes -= 1

blueprints = []
for n in range(len(input)):
    mining = input[n].split(": ")[1].split(". ")
    blueprint = int(input[n].split(": ")[0].split(" ")[1])
    ore_robot = int(mining[0].split(" ")[4])
    clay_robot = int(mining[1].split(" ")[4])
    obsidian_robot_rO = int(mining[2].split(" ")[4])
    obsidian_robot_rC = int(mining[2].split(" ")[7])
    geode_robot_rO = int(mining[3].split(" ")[4])
    geode_robot_rOB = int(mining[3].split(" ")[7])


    blueprints.append(Blueprint(blueprint,ore_robot,clay_robot,obsidian_robot_rO,
        obsidian_robot_rC,geode_robot_rO,geode_robot_rOB))
    

upgrade = ['geode', 'obs', 'clay', 'ore']
from itertools import combinations
print(combinations(upgrade,4))

for n in list(combinations(upgrade,4)):
    print(n)

for i,k,k,l in 
for bp in blueprints:
    while bp.minutes > 0:
        bp.collect()
        bp.simulate()

sum = 0
for bp in blueprints:
    print("RES=",bp.ore,bp.clay,bp.obs,bp.geode)
    print("robots=",bp.robot_ore,bp.robot_clay,bp.robot_obs,bp.robot_geode)
    print(bp.bp,bp.geode,bp.bp*bp.geode)
    print("--------------")
    sum += bp.bp*bp.geode
print(sum)



s_location = [k for k, v in input.items() if v == -13][0]
finish_location = [k for k, v in input.items() if v == -27][0]

input[s_location], input[finish_location] = 1, 26

def bfs(input):
    visited = {finish_location: 0}
    queue = [finish_location]
    while queue:
        (x, y) = queue.pop(0)
        check_moves = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        for move in check_moves:
            if (move in input and not move in visited) and input[(x, y)] - input[move] <= 1:
                visited[move] = visited[(x, y)] + 1
                queue.append(move)
    return(visited, s_location)

d, s= bfs(input)
print(d[s])

low_value = 450
input2 = dict()
for n in input.items():
    if input[n[0]] == 1 and n[0] in d and d[n[0]] < low_value:
        low_value = d[n[0]]
print(low_value)


