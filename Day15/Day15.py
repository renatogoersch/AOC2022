with open('input_day15.csv') as file:
#with open('ti.csv') as file:
    input_day15 = [line.rstrip() for line in file]

x,y = [],[]
sum = 0
places = []
xy_beacon = []
xy_sensor = []

def distm(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance


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
    xy_beacon.append((int(beacon_x),int(beacon_y)))
    xy_sensor.append((int(sensor_x),int(sensor_y)))

    dist_y = abs(int(sensor_y) - int(beacon_y))
    dist_x = abs(int(sensor_x) - int(beacon_x))
    dist = int(distm((sensor_x,sensor_y),(beacon_x,beacon_y)))
    #print(dist)
    valuex = 2000000
    #print("Sensor:",sensor_x,sensor_y)
    #print("Beacon:",beacon_x,beacon_y)
    #print("Distancia:",str(dist))
    #print("Range:",str(sensor_y),str(sensor_y+dist))
    for value in range(sensor_y,sensor_y+dist+1):
        if value == valuex:
            if sensor_y > value:
                rangex = sensor_y - value
            elif sensor_y < value:
                rangex = value - sensor_y
            #print("Rangex:",rangex)
            range1 = (sensor_x - (dist - rangex))
            #print("Range 1:",range1)
            range2 = (sensor_x + (dist - rangex) + 1)
            #print("Range 2:",range2)
            for i in range(range1,range2):
                places.append((i,valuex))
                #print("when y ==:",i)

    for value in range(sensor_y-dist,sensor_y):
        if value == valuex:
            if sensor_y > value:
                rangex = sensor_y - value
            elif sensor_y < value:
                rangex = value - sensor_y
            #print("Rangex:",rangex)
            range1 = (sensor_x - (dist - rangex))
            #print("Range 1:",range1)
            range2 = (sensor_x + (dist - rangex) + 1)
            #print("Range 2:",range2)
            for i in range(range1,range2):
                places.append((i,valuex))
                #print("when y ==:",i)

places = list(dict.fromkeys(places))
xy_beacon = list(dict.fromkeys(xy_beacon))
xy_sensor = list(dict.fromkeys(xy_sensor))
#print(len(places))
#print(len(xy_beacon))

print(len(results))


