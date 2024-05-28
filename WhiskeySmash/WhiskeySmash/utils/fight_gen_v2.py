import pandas as pd
import random

member = pd.read_csv('WhiskeySmash/CSV/WW_MEMBER_202405281145.csv')
member_fighters = pd.read_csv('WhiskeySmash/CSV/fighter_wheel_202405281145.csv')
fighters = pd.read_csv('WhiskeySmash/CSV/FIGHTER_202405281145.csv')



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
    scrubbed_fight_list = []
    for k,v in randomized_fight_dict.items():
        scrubbed_fight_list.append([k,v])
    for t in scrubbed_fight_list:
    #<set up temporary list to compare to others
        for c in scrubbed_fight_list:
            #<set up compared list
            if t[0] == c[0]:
                continue
            else:
                #< compare list indicies and remove highest index duplicate. if equal remove both!
                for x in t[1]:
                    if x in c[1]:
                        comp_a = t[1].index(x)
                        comp_b = c[1].index(x)
                        if comp_a < comp_b:
                            c[1].remove(x)
                        elif comp_b < comp_a:
                            t[1].remove(x)
                        else:
                            t[1].remove(x)
                            c[1].remove(x)
    return dict(scrubbed_fight_list)