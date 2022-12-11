os.chdir(r"C:\Users\renat\Documents\AOC2022\AOC2022\Day10")

with open('input_day10.csv') as file:
    input_day10 = [line.rstrip() for line in file]
values_to_add = []
cycles = 0

for n in range(0,len(input_day10)):
    if ' ' in input_day10[n]:
        cycles += 2
        add_value = [cycles,int(input_day10[n].split(" ")[1])]
        values_to_add.insert(0,add_value)
    else:
        cycles += 1


def check_signal(signal_value,values_to_add,cycles,signals):
    sum_signal=0
    for n in range(cycles):
        for i in range(len(values_to_add)):
            if values_to_add[i][0] == n:
                signal_value += values_to_add[i][1]
        if (n+1) in signals:
            sum_signal+=signal_value*(n+1)
    return sum_signal
signal_value=1
sum = check_signal(signal_value,values_to_add,cycles,[20,60,100,140,180,220])
print(sum)


signal_value=1
row_cycles = int(cycles/40)
for r in range(1,row_cycles+1):
    printx = [' ']*40
    for n in range((r-1)*40,(r*40)):
        for i in range(len(values_to_add)):
            #print(n)
            if values_to_add[i][0] == n:
                signal_value += values_to_add[i][1]
        pos = n - ((r-1)*40)
        if signal_value in range(pos-1,pos+2):
            printx[pos] = "#"
    printx = ''.join(printx)
    print(printx)




