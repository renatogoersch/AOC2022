import sys
with open('input_day18.csv') as file:
#with open('ti.csv') as file:
    cubs = {tuple(int(x) for x in line.split(',')) for line in file}

def around(point, min_v, max_v):
    x, y, z = point
    list_poss = set()
    if x > min_v:
        list_poss.add((x - 1, y, z))
    if x < max_v:
        list_poss.add((x + 1, y, z))
    if y > min_v:
        list_poss.add((x, y - 1, z))
    if y < max_v:
        list_poss.add((x, y + 1, z))
    if z > min_v:
        list_poss.add((x, y, z - 1))
    if z < max_v:
        list_poss.add((x, y, z + 1))
    return list_poss

min_v = min(min(point) for point in cubs) - 1
max_v = max(max(point) for point in cubs) + 1

result1 = 6 * len(cubs)
for point in cubs:
    result1 -= len(around(point, min_v, max_v) & cubs)
print("Parte 1:", result1)

result2 = 0
b = [(min_v, min_v, min_v)]
p = {b[0]}
while b:
    point = b.pop()
    for other in around(point, min_v, max_v) - p:
        if other in cubs:
            result2 += 1
        else:
            p.add(other)
            b.append(other)
print("Parte 2:", result2)