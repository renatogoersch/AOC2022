import pandas as pd
os.chdir(r"C:\Users\renat\Documents\AOC2022\AOC2022\Day8")

input_day8 = pd.read_csv('input_day8.csv', sep=',', header=None)
#input_day8 = pd.read_csv('ti.csv', sep=',', header=None)
input_day8[0] = input_day8[0].astype(str)
input_day8 = input_day8[0].str.split("", expand=True,)
input_day8 = input_day8.drop(labels=[0, 100], axis=1)
#input_day8 = input_day8.drop(labels=[0, 6], axis=1)
input_day8.index = input_day8.index + 1

count = 0
higher_x = 0
higher_y = 0

def check_higher(height,df_height):
    list_height = []
    for sublist in df_height:
        if type(sublist) == str:
            list_height.append(int(sublist))
        if type(sublist) == int:
            list_height.append(sublist)
        elif type(sublist) == list:
            for item in sublist:
                list_height.append(int(item))
    if int(height) > max(list_height):
        return True
    
        
def check_is_visible(x,y,input):
    if y != len(input.columns):
        r_is_visible1 = check_higher(input.iloc[x,y],
            input.iloc[x,y+1:len(input.columns)])
    else:
        r_is_visible1 = False
    
    if x != len(input_day8):
        d_is_visible2 = check_higher(input.iloc[x,y],
            input.iloc[x+1:len(input),y])
    else:
        d_is_visible2 = False
    if y != 0:
        l_is_visible3 = check_higher(input.iloc[x,y],
            input.iloc[x,0:y])
    else:
        l_is_visible3 = False
    
    if x != 0:
        t_is_visible4 = check_higher(input.iloc[x,y],
            input.iloc[0:x,y])
    else:
        t_is_visible4 = False

    if r_is_visible1 == True or d_is_visible2 == True or l_is_visible3 == True or t_is_visible4 == True:
        return True
    

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

def Right_view(height,df_height):
    count = 0
    list_height = []
    for sublist in df_height:
        list_height.append(int(sublist))
    for n in list_height:
        if height > n:
            count += 1
        else:
            count += 1
            return count
    return count

def Down_view(height,df_height):
    count = 0
    list_height = []
    for sublist in df_height:
        list_height.append(int(sublist))
    for n in list_height:
        if height > n:
            count += 1
        else:
            count += 1
            return count
    return count

def Left_view(height,df_height):
    df_height = Reverse(df_height)
    count = 0
    list_height = []
    for sublist in df_height:
        list_height.append(int(sublist))
    for n in list_height:
        if height > n:
            count += 1
        else:
            count += 1
            return count
    return count

def Top_view(height,df_height):
    df_height = Reverse(df_height)
    print(df_height)
    count = 0
    list_height = []
    for sublist in df_height:
        list_height.append(int(sublist))
    print(list_height)
    for n in list_height:
        if height > n:
            count += 1
        else:
            count += 1
            return count
    return count


def get_view(x,y,input):
    if y != len(input.columns):
        right_view = Right_view(int(input.iloc[x,y]),
            input.iloc[x,y+1:len(input.columns)])
    else:
        right_view = 0
    if x != len(input_day8):
        down_view = Down_view(int(input.iloc[x,y]),
            input.iloc[x+1:len(input),y])
    else:
        down_view = 0
    if y != 0:
        left_view = Left_view(int(input.iloc[x,y]),
            input.iloc[x,0:y])
    else:
        left_view = 0
    if x != 0:
        top_view = Top_view(int(input.iloc[x,y]),
            input.iloc[0:x,y])
    else:
        top_view = 0
    #print(str(right_view) + "," + str(down_view) + "," + str(left_view) + "," + str(top_view))
    return (right_view * down_view * left_view * top_view)

def call_step1(input_day8):
    count = 0
    highest_view_value = 0
    for x in range(0,len(input_day8)):
        for y in range(0,len(input_day8.columns)):
            view_value = get_view(x,y,input_day8)
            print(view_value)
            if view_value > highest_view_value:
                highest_view_value = view_value
            if x == 0 or x == len(input_day8)-1:
                count += 1
            elif y == 0 or y == len(input_day8.columns)-1:
                count += 1
            else:
                is_visible = check_is_visible(x,y,input_day8) 
                if is_visible == True:
                    #print(str(x) + "," + str(y) + " - " + input_day8.iloc[x,y])
                    count += 1
    return count,highest_view_value

print(call_step1(input_day8))
