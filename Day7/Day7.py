import pandas as pd
os.chdir(r"C:\Users\Renato Parente\Documents\AdventOfCode\AOC2022\Day7")

with open('input_day7.csv') as file:
    input_day7 = [line.rstrip() for line in file]

dirs = pd.DataFrame(columns=['path','name','size'])
dirs_list = pd.DataFrame(columns=['path','size'])

def add_paths(dirs,path,name,size):
    new_row = {'path':path, 'name':name, 'size':size}
    dirs = dirs.append(new_row, ignore_index=True)
    return dirs

def add_dirs(dirs_list,path,size):
    new_row = {'path':path, 'size':size}
    dirs_list = dirs_list.append(new_row, ignore_index=True)
    return dirs_list

path = "/"
dirs_list = add_dirs(dirs_list,path,0)
for n in input_day7:
    if '$ cd /' in n:
        npath = n.replace('$ cd ','')
        path = npath
    elif '$ cd ..' in n:
        npath = path.split("/")
        npath = npath[:-1]
        npath = "/".join(npath)
        path = npath
    elif '$ cd' in n and '/' not in n:
        if path == '/':
            npath = n.replace('$ cd ','')
            path = path + npath
        else:
            npath = n.replace('$ cd ','')
            path = path + "/" + npath
    elif '$ ls' in n:
        pass
    elif 'dir ' in n:
        size = 0
        if path == '/':
            npath = "/" + n.replace('dir ','')
        else:
            npath = path + "/" + n.replace('dir ','')
        dirs_list = add_dirs(dirs_list,npath,int(size))
    else:
        size = int(n.split(" ")[0])
        dirs = add_paths(dirs,path,n.split(" ")[1],int(size))

for n in range(len(dirs_list['path'])):
    path = dirs_list['path'][n]
    #dirs_s = dirs.query('path==@path')['size'].sum()
    dirs_s = dirs.query('path.str.contains(@path)', engine='python')['size'].sum()
    dirs_list['size'][n] = dirs_s

folders = dirs_list.query('size<=100000')
folders_sum = folders['size'].sum()
print("Resultado da Primeira Parte: " + str(folders_sum))


dirs_list = dirs_list.sort_values(['size'], ascending=False)
space_to_free = 30000000 - (70000000 - dirs_list['size'][0])
possible_list_to_Free = dirs_list.query('size>=@space_to_free')
possible_list_to_Free = possible_list_to_Free.sort_values(['size'], ascending=True).reset_index()
print("Resultado da Primeira Parte: " + str(possible_list_to_Free['size'][0]))
