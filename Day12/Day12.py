input = open("input_day12.csv").read().rstrip().split()
input = {(x, y) : ord(L) - 96 for y, _ in enumerate(input)
        for x, L in enumerate(_)}


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