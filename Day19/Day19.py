import random
#with open('input_day19.csv') as file:
with open('ti.csv') as file:
    input = [line.rstrip() for line in file]

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
data1 = list('1000')
data2 = list('1100')
data3 = list('1110')
data4 = list('1111')
data5 = list('0000')
pos = permutation(data1)
data2 = permutation(data2)
data3 = permutation(data3)
for n in data2:
    pos.append(n)
for n in data3:
    pos.append(n)
pos.append(data4)
pos.append(data5)

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
            self.minutes = 0
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

            #print("Created a Blueprint number",self.bp)

    def collect(self):
        self.ore += 1*self.robot_ore
        self.clay += 1*self.robot_clay
        self.obs += 1*self.robot_obs
        self.geode += 1*self.robot_geode

    def upgrade_geode(self,todo):
        if todo == '1':
            if self.ore >= self.recipe_grr.ore and self.obs >= self.recipe_grr.obs:
                self.ore -= self.recipe_grr.ore
                self.obs -= self.recipe_grr.obs
                self.robot_geode += 1

    def upgrade_obs(self,todo):
        if todo == '1':
            if self.ore >= self.recipe_obrr.ore and self.clay >= self.recipe_obrr.clay and self.robot_obs < 2:
                self.ore -= self.recipe_obrr.ore
                self.clay -= self.recipe_obrr.clay
                self.robot_obs += 1

        
    def upgrade_clay(self,todo):
        if todo == '1' and self.robot_clay < 4:
            if self.ore >= self.recipe_crr.ore:
                self.ore -= self.recipe_crr.ore
                self.robot_clay += 1


    def upgrade_ore(self,todo):
        if todo == '1' and self.robot_ore < 1:
            if self.ore >= self.recipe_orr.ore:
                self.ore -= self.recipe_orr.ore
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
        global max_geode, max_obs, max_clay, max_ore
        restore = [self.robot_ore, self.robot_clay,
        self.robot_obs, self.robot_geode,
        self.ore, self.clay,
        self.obs, self.geode, self.minutes]

        to_check = pos
        to_do = [[[],'']]*24
        to_real_do = []*24
        self.minutes = 0
        while self.minutes < 24:
            for n in to_check:
                self.collect
                self.restore(restore)
                self.upgrade_geode(n)
                self.upgrade_obs(n)
                self.upgrade_clay(n)
                self.upgrade_ore(n)
                print(self.minutes)
                to_do[self.minutes-1][0].append(n)
                to_do[self.minutes-1][1] = self.robot_geode
                self.minutes += 1
                print(self.minutes)
                if (self.robot_geode > max_geode):
                    max_geode = self.robot_geode
                    to_do = n
                else:
                    if (self.robot_obs > max_obs):
                        max_obs = self.robot_obs
                        to_do = n
                    else:
                        if (self.robot_clay > max_clay):
                            max_clay = self.robot_clay
                            to_do = n
                        else:
                            if (self.robot_ore > max_ore):
                                max_ore = self.robot_ore
                                to_do = n
        self.restore(restore)
        return to_do

    def cicle(self, to_do):
        print(to_do)
        self.upgrade_geode(to_do[self.minutes])
        self.upgrade_obs(to_do[self.minutes])
        self.upgrade_clay(to_do[self.minutes])
        self.upgrade_ore(to_do[self.minutes])
        
                
    def restore(self,restore):
        self.robot_ore = restore[0]
        self.robot_clay = restore[1]
        self.robot_obs = restore[2]
        self.robot_geode = restore[3]
        self.ore = restore[4]
        self.clay = restore[5]
        self.obs = restore[6]
        self.geode = restore[7]

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

for bp in blueprints:
    max_geode = bp.robot_geode
    max_obs = bp.robot_obs
    max_clay = bp.robot_clay
    max_ore = bp.robot_ore
    bp.minutes = 24
    to_do = bp.simulate()
    while bp.minutes > 0:
        bp.collect()
        bp.cicle(to_do)
        print("----",bp.bp,"----")
        print("Minute",bp.minutes)
        print("ores:",bp.ore,"robos:",bp.robot_ore)
        print("clay:",bp.clay,"robos:",bp.robot_clay)
        print("obs:",bp.obs,"robos:",bp.robot_obs)
        print("geodes:",bp.geode,"robos:",bp.robot_geode)
        print("--------")
        bp.minutes -= 1

sum = 0
for bp in blueprints:
    print("RES=",bp.ore,bp.clay,bp.obs,bp.geode)
    print("robots=",bp.robot_ore,bp.robot_clay,bp.robot_obs,bp.robot_geode)
    print(bp.bp,bp.geode,bp.bp*bp.geode)
    print("--------------")
    sum += bp.bp*bp.geode
    print(sum)
#print(sum)

