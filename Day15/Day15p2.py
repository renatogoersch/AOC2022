with open('input_day15.csv') as file:
#with open('ti.csv') as file:
    input_day15 = [line.rstrip() for line in file]

x,y = [],[]
sum = 0
places = []
xy_beacon = []
xy_sensor = []
part2 = []

def distm(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance

ranges = []
for row in input_day15:
    print(row)
    sensor = row.split(':')[0].split('at ')[1].split(', ')
    sensor_x = int(sensor[0].split('=')[1])
    sensor_y = int(sensor[1].split('=')[1])
    beacon = row.split(':')[1].split('at ')[1].split(', ')
    beacon_x = int(beacon[0].split('=')[1])
    beacon_y = int(beacon[1].split('=')[1])
    #print(sensor_x,sensor_y,beacon_x,beacon_y)
    x.append(int(sensor_x))
    x.append(int(beacon_x))
    y.append(int(sensor_y))
    y.append(int(beacon_y))
    dist_y = abs(int(sensor_y) - int(beacon_y))
    dist_x = abs(int(sensor_x) - int(beacon_x))
    dist = int(distm((sensor_x,sensor_y),(beacon_x,beacon_y)))
    xy_beacon.append((int(beacon_x),int(beacon_y),dist))
    xy_sensor.append((int(sensor_x),int(sensor_y),dist))
    part2.append((int(sensor_x),int(sensor_y),int(beacon_x),int(beacon_y),dist))


xy_beacon = list(dict.fromkeys(xy_beacon))
xy_sensor = list(dict.fromkeys(xy_sensor))

rng = range(4000001)
middle = rng.stop // 2
covered_by_sensors = []
search = []

for n in part2:
    sx, sy, bx, by = n[0], n[1], n[2], n[3]
    coverage = n[4]
    dy = abs(sy - middle)
    dx = coverage - dy
    if dx > 0:
        covered_by_sensors.append([range(sx - dx, sx + dx + 1)])
    for cy in range(max(rng.start, sy - coverage - 1), min(rng.stop, sy + 1)):
        dx = coverage + cy - sy + 1
        search.append([(max(rng.start, sx - dx), cy)])
        search.append([(min(rng.stop, sx + dx + 1), cy)])
    for cy in range(min(rng.stop, sy + coverage + 1), max(rng.start, sy), -1):
        dx = coverage - cy + sy + 1
        search.append([(max(rng.start, sx - dx), cy)])
        search.append([(min(rng.stop, sx + dx + 1), cy)])
for loc in search:
    for s in xy_sensor:
        distance = abs(s[0] - loc[0][0]) + abs(s[1] - loc[0][1])
        if distance <= coverage:
            break
    else:
        break
print(4_000_000 * y[0] + y[1])