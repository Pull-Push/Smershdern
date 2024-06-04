import pandas as pd
import random

member = pd.read_csv('WhiskeySmash/CSV/WW_MEMBER_202406032045.csv')
member_fighters = pd.read_csv('WhiskeySmash/CSV/fighter_wheel_202406032045.csv')
fighters = pd.read_csv('WhiskeySmash/CSV/FIGHTER_202406032045.csv')

#! MAX FIGHTS PER PLAYER - 2p 41, 3p 27, 4p 20, 5p 16, 6p 13, 7p 11, 8p 10



#< Verifies players are in member db file
def fight_setup(*args):
    merged_v1 = member.merge(member_fighters, how='inner', on='member_id')
    merged_v2 = merged_v1.merge(fighters, how='inner', on='FIGHTER_ID')
    ind_smash_list = merged_v2.groupby(['member_name'])
    final_dict = {"PLAYER":{}}
    #<GET FIGHTER LIST FOR EACH MEMBER IN INITIALIZATION
    member_list = args
    found_fighters = merged_v2[merged_v2['member_name'].isin(member_list)]
    named_found_fighters = set(found_fighters['member_name'])
    for x in named_found_fighters:
        final_dict['PLAYER'][x] = {"FIGHTERS":[]}
    #<Creates dictionary for each verified played
    #<Populates dictionary value with randomized list of personal smash characters
    match_fighters = []
    for x in final_dict['PLAYER']:
        player_fighter_list = random.sample(list(ind_smash_list.get_group((x,))['FIGHTER_NAME']), len(list(ind_smash_list.get_group((x,))['FIGHTER_NAME'])))
        match_fighters.append(player_fighter_list)
        final_dict['PLAYER'][x]['FIGHTERS'] = player_fighter_list
    #< REMOVE DUPES FROM EACH LIST  - Get index of dupes and remove latter
    for tk,tv in final_dict['PLAYER'].items():
        for ck, cv in final_dict['PLAYER'].items():
            if tk == ck:
                continue
            else:
                # print('comparing', tk, 'to', ck)
                # print('test fighter', tv['FIGHTERS'])
                # print('compare fighter', cv['FIGHTERS'])
                for tm in tv['FIGHTERS']:
                    if tm in cv['FIGHTERS']:
                        comp_a = tv['FIGHTERS'].index(tm)
                        comp_b = cv['FIGHTERS'].index(tm)
                        if comp_a < comp_b:
                            cv['FIGHTERS'].remove(tm)
                        elif comp_b < comp_a:
                            tv['FIGHTERS'].remove(tm)
                        else:
                            tv['FIGHTERS'].remove(tm)
                            cv['FIGHTERS'].remove(tm)
    total_match_fighters = []
    for x in match_fighters:
        for y in x:
            total_match_fighters.append(y)
    print('match_fighter',total_match_fighters)
    # # print('all fighters', list(fighters["FIGHTER_NAME"]))
    remainder_fighters = []
    #< FIX PIKA REF!!!!! DONE
    for af in list(fighters["FIGHTER_NAME"]):
        if af in total_match_fighters:
            continue
        else:
            print('not found', af)
    return final_dict


# def evenout(dict):
#     #GET MAX LENGTH OF ALL FIGHTER LISTS
#     max = 0 
#     for k,v in dict['PLAYER'].items():
#         if len(v['FIGHTERS']) >= max:
#             max = len(v["FIGHTERS"])
#         # print(k, len(v["FIGHTERS"]))
#     #GET LIST OF CHARACTERS NOT ASSOCIATED WITH PLAYERS
#     return

fight_setup(str.title('Sokol'),str.title('Reen'),str.title("Joe"))