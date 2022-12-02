import pandas as pd
import os

os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day2")

# LOAD AND CLEAN DATA
input_day2 = pd.read_csv('input_day2.csv', sep=';')

#Regras
### A>Z
### A=X
### A<Y

### B>X
### B=Y
### B<Z

### C>Y
### C=Z
### C<X

#A e X = 1
#B e Y = 2
#C e Z = 3

#A e X = ROCK
#B e Y = PAPER
#C e Z = SCISSORS

## Implementação segunda parte
def new_moves(row):
    if row['P2'] == "X":
        if row['P1'] == "A":
            return "Z"
        if row['P1'] == "B":
            return "X"
        if row['P1'] == "C":
            return "Y"
    if row['P2'] == "Y":
        if row['P1'] == "A":
            return "X"
        if row['P1'] == "B":
            return "Y"
        if row['P1'] == "C":
            return "Z"
    if row['P2'] == "Z":
        if row['P1'] == "A":
            return "Y"
        if row['P1'] == "B":
            return "Z"
        if row['P1'] == "C":
            return "X"

# Quem vence cada match? e Quantos pontos cada um recebe?
def who_win(row):
    if row['P1'] == "A":
        if row['P2'] == "Z":
            return pd.Series(['P1', 7, 3])
        if row['P2'] == "X":
            return pd.Series(['Draw', 4, 4])
        if row['P2'] == "Y":
            return pd.Series(['P2', 1, 8])

    if row['P1'] == "B":
        if row['P2'] == "X":
            return pd.Series(['P1', 8, 1])
        if row['P2'] == "Y":
            return pd.Series(['Draw', 5, 5])
        if row['P2'] == "Z":
            return pd.Series(['P2', 2, 9])

    if row['P1'] == "C":
        if row['P2'] == "Y":
            return pd.Series(['P1', 9, 2])
        if row['P2'] == "Z":
            return pd.Series(['Draw', 6, 6])
        if row['P2'] == "X":
            return pd.Series(['P2', 3, 7])

input_day2_new = input_day2.copy()
input_day2_new['P2'] = input_day2_new.apply(lambda row: new_moves(row), axis=1)

input_day2[['Winner', 'Points_P1', 'Points_P2']] = input_day2.apply(lambda row: who_win(row), axis=1)
input_day2_new[['Winner', 'Points_P1', 'Points_P2']] = input_day2_new.apply(lambda row: who_win(row), axis=1)

results = input_day2['Points_P2'].sum()
results2 = input_day2_new['Points_P2'].sum()

print("Resultados da Primeira Parte: " + str(results))
print("Resultados da Segunda Parte: " + str(results2))