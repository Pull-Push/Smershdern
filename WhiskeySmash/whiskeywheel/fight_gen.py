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
    named_found_fighters = set(found_fighters['member_name'])
    fight_dict = {}
    for x in named_found_fighters:
        fight_dict[x] = []
    #linked member to custom wheel
    linked = list(zip(list(found_fighters['member_name']), list(found_fighters['member_id'])))
    for k,v in linked:
        for x in member_fighters.values:
            if v == x[1]:
                fight_dict[k].append(x[2])
# # #! link player dictionary values to fighter numbers
    print(fight_dict)
#     for x in fight_dict.values():
#         print(x)
#         fighter_name = fighters[fighters['FIGHTER_NUMBER']==x]['FIGHTER_NAME']
#         print(fighter_name)


#     print(fight_dict)
    return


# print(member.head())
fight_setup(str.title('sokol'), str.title('reen'), str.title('Steve'), str.title('joe'), str.title('bill'))