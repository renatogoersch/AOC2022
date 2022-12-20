#with open('day19_input.csv') as file:
with open('ti.csv') as file:
    input = [line.rstrip() for line in file]

# 1 obsidian <- 1 obsidian-collecting robots
# 1 clay <- 1 clay-collecting robots
# 1 clay-collecting robots <- 1 ore
# 1 ore <- ore-collecting robots

ore-collecting-robot = 1
# Each robot can collect 1 of its resource type per minute.
# t also takes one minute for the robot factory 
# (also conveniently from your pack) to construct any type of robot

minutes = 24

for n in len((input-1)/5):
    ore_robot = int(input[n+1].split(" ")[7])
    ore_robot = int(input[n+2].split(" ")[7])
    ore_robot = int(input[n+3].split(" ")[10])
    ore_robot = int(input[n+3].split(" ")[7])
    ore_robot = int(input[n+3].split(" ")[10])
