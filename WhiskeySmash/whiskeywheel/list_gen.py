import pandas as pd
import random

member = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/WW_MEMBER_202405142034.csv')
member_fighters = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/fighter_wheel_202405142034.csv')
fighters = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/FIGHTER_202405142034.csv')
joe_fights= []
reen_fights = []
sok_fights = []

for x in member_fighters.values:
    if x[1] == 1:
        joe_fights.append(x[2])
    elif x[1] == 2:
        reen_fights.append(x[2])
    elif x[1] == 3:
        sok_fights.append(x[2])

def fighter_list(arr):
    temp = []
    for x in arr:
        if x in fighters['FIGHTER_NUMBER']:
            temp.append(fighters['FIGHTER_NAME'][x-1])
    arr = temp
    return arr

def randomize_fighters(list):
    temp = fighter_list(list)
    random.shuffle(temp)
    list = temp
    return list

def create_smersh(*args):
    result = []
    for x in args:
        result.append(randomize_fighters(x))
    return result
    
def remove_dupes(*args):
    total_arg_len = len(args[0])
    arg_counter = 0
    while arg_counter < total_arg_len-1:
        for x in args[0][arg_counter]:
            if x in args[0][arg_counter+1]:
                print(x)
                print(args[0][arg_counter].index(x))
                print(args[0][arg_counter+1].index(x))
                
        arg_counter += 1
    return


print(create_smersh(joe_fights,reen_fights, sok_fights))

# remove_dupes(create_smersh(joe_fights, reen_fights))
