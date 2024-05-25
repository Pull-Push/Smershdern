import pandas as pd
import random

member = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/WW_MEMBER_202405142034.csv')
member_fighters = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/fighter_wheel_202405142034.csv')
fighters = pd.read_csv('WhiskeySmash/whiskeywheel/CSV/FIGHTER_202405142034.csv')


#< Verifies players are in member db file
def fight_setup(*args):
    merged_v1 = member.merge(member_fighters, how='inner', on='member_id')
    merged_v2 = merged_v1.merge(fighters, how='inner', on='FIGHTER_ID')
    ind_smash_list = merged_v2.groupby(['member_name'])
    #<GET FIGHTER LIST FOR EACH MEMBER IN INITIALIZATION
    member_list = args
    found_fighters = merged_v2[merged_v2['member_name'].isin(member_list)]
    named_found_fighters = set(found_fighters['member_name'])
    #<Creates dictionary for each verified played
    fight_dict = {}
    #<Populates dictionary value with list of smash characters
    for x in named_found_fighters:
        fight_dict[x] = (list(ind_smash_list.get_group(x)['FIGHTER_NAME']))
    #< RANDOMIZE EACH LIST
    randomized_fight_dict = {}
    for k,v in fight_dict.items():
        new_v = random.sample(v, len(v))
        randomized_fight_dict[k] = new_v
    #< REMOVE DUPES FROM EACH LIST  - Get index of dupes and remove latter
    #!NOT WORKING. NEED TO FIND WAY TO CHECK 1 and 3
    #pseduo - make temp list of number 1 then check all others. advance temp and check again
    scrubbed_fight_list = []
    for k,v in randomized_fight_dict.items():
        scrubbed_fight_list.append([k,v])

    return scrubbed_fight_list


fight_setup(str.title('sokol'), str.title('reen'), str.title('Steve'), str.title('joe'), str.title('bill'))
# print(fight_setup(str.title('sokol'), str.title('reen'), str.title('Steve'), str.title('joe'), str.title('bill')))