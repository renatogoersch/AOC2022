import pandas as pd
import os
import math


os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day4")

input_day4 = pd.read_csv('input_day4.csv', sep=',', names=['E1','E2'])


input_day4['Check'] = 0
input_day4['Check2'] = 0
for i in range(0,input_day4['E1'].size):
    num1 = int(input_day4['E1'][i].split('-')[0])
    num2 = int(input_day4['E1'][i].split('-')[1])
    num3 = int(input_day4['E2'][i].split('-')[0])
    num4 = int(input_day4['E2'][i].split('-')[1])
    count_c = (num4 - num3) + 1
    count_c2 = 0
    for n in range(num1-1,num2):
        if n in range(num3-1,num4):
            count_c2 += 1
    if count_c2 == count_c:
        input_day4['Check'][i] = 1
    if count_c2 > 0:
        input_day4['Check2'][i] = 1
    count_c = (num2 - num1) + 1
    count_c2 = 0
    for n in range(num3-1,num4):
        if n in range(num1-1,num2):
            count_c2 += 1
    if count_c2 == count_c:
        input_day4['Check'][i] = 1
    if count_c2 > 0:
        input_day4['Check2'][i] = 1


results = input_day4['Check'].sum()
print("Resultados da Primeira Parte: " + str(results))
results2 = input_day4['Check2'].sum()
print("Resultados da Segunda Parte: " + str(results2))
