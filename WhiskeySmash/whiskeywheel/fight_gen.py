import pandas as pd
import random

member = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/WW_MEMBER_202405142034.csv')
# print(member.head())
member_fighters = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/fighter_wheel_202405142034.csv')
# print(member_fighters.head())
fighters = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/FIGHTER_202405142034.csv')

#< Verifies players are in member db file
def fight_setup(*args):
    #!GET FIGHTER LIST FOR EACH MEMBER IN INITIALIZATION
    member_list = args
    found_fighters = member[member['member_name'].isin(member_list)]
    # print(list(found_fighters['member_id']), list(found_fighters['member_name']))
    linked = list(zip(list(found_fighters['member_name']), list(found_fighters['member_id'])))
    # print(linked)
    #todo fix this. is broken
    for k,v in linked:
        for i in member_fighters["member_id"]:
            if v == i:
                print(v)

    named_found_fighters = set(found_fighters['member_name'])
    #<establish list for each member
    fight_dict = {}
    for x in named_found_fighters:
        fight_dict[x] = []
    # print(fight_dict)
    return


# print(member.head())
fight_setup(str.title('sokol'), str.title('reen'), str.title('Steve'), str.title('joe'), str.title('bill'))