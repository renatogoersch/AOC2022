import pandas as pd
import os
import math


os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day3")


input_day3 = pd.read_csv('input_day3.csv', sep=';')


def size(row):
    return len(row['Input'])


def first_half(row):
    return row['Input'][0:int(len(row['Input'])/2)]


def second_half(row):
    return row['Input'][int(len(row['Input'])/2):len(row['Input'])]


input_day3['size'] = input_day3.apply(lambda row: size(row), axis=1)
input_day3['FH'] = input_day3.apply(lambda row: first_half(row), axis=1)
input_day3['SH'] = input_day3.apply(lambda row: second_half(row), axis=1)

priority_list = {'a': 1, 'b': 2, 'c': 3, 
                'd': 4, 'e': 5, 'f': 6, 
                'g': 7, 'h': 8, 'i': 9, 
                'j': 10, 'k': 11, 'l': 12, 
                'm': 13, 'n': 14, 'o': 15, 
                'p': 16, 'q': 17, 'r': 18, 
                's': 19, 't': 20, 'u': 21, 
                'v': 22, 'w': 23, 'x': 24, 
                'y': 25, 'z': 26, 'A': 27, 
                'B': 28, 'C': 29, 'D': 30, 
                'E': 31, 'F': 32, 'G': 33, 
                'H': 34, 'I': 35, 'J': 36, 
                'K': 37, 'L': 38, 'M': 39, 
                'N': 40, 'O': 41, 'P': 42, 
                'Q': 43, 'R': 44, 'S': 45, 
                'T': 46, 'U': 47, 'V': 48, 
                'W': 49, 'X': 50, 'Y': 51,
                'Z': 52}


def check_compartments(row):
    both_comp = ""
    for s in row['FH']:    
        for s2 in row['SH']:
            if s == s2:
                if s not in both_comp:
                    both_comp = both_comp + s
    return both_comp


def check_priorities(row):
    return priority_list[row['Both_compartments']]


input_day3['Both_compartments'] = input_day3.apply(lambda row: check_compartments(row), axis=1)
input_day3['Priority'] = input_day3.apply(lambda row: check_priorities(row), axis=1)
results = input_day3['Priority'].sum()
print("Resultados da Primeira Parte: " + str(results))
input_day3['Group'] = ""


def check_groups():
    for n in range(input_day3['Input'].size):
        input_day3['Group'][n] = math.ceil((n+1)/3)


check_groups()


input_day3['Common_item'] = ""


def check_each_groups():
    for n in range(1,101):
        check = input_day3.query("Group == @n")
        for s in check['Input'][check.index[0]]:    
            for s2 in check['Input'][check.index[1]]:
                for s3 in check['Input'][check.index[2]]:
                    if s == s2 and s2 == s3:
                        if s not in input_day3.loc[check.index, "Common_item"]:
                            input_day3.loc[check.index, "Common_item"] = s


check_each_groups()


groups = input_day3[['Group','Common_item']].drop_duplicates()


def check_prioritiesg(row):
    return priority_list[row['Common_item']]


groups['Priority'] = groups.apply(lambda row: check_prioritiesg(row), axis=1)
results2 = groups['Priority'].sum()
print("Resultados da Primeira Parte: " + str(results2))