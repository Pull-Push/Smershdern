import pandas as pd
import random

member = pd.read_csv('WhiskeySmash/CSV/WW_MEMBER_202406042059.csv')
member_fighters = pd.read_csv('WhiskeySmash/CSV/fighter_wheel_202406042059.csv')
fighters = pd.read_csv('WhiskeySmash/CSV/FIGHTER_202406042059.csv')



#< Verifies players are in member db file
def fight_setup(*args):
    fight_total = {2:41, 3:27, 4:20, 5:16, 6:13, 7:11, 8:10}
    merged_v1 = member.merge(member_fighters, how='inner', on='member_id')
    merged_v2 = merged_v1.merge(fighters, how='inner', on='FIGHTER_ID')
    ind_smash_list = merged_v2.groupby(['member_name'])
    final_dict = {"PLAYER":{}}
    #<GET FIGHTER LIST FOR EACH MEMBER IN INITIALIZATION
    member_list = args
    if member_list == ('', '', '', '', '', '', '', ''):
        member_list = (('Player 1', 'Player 2', '', '', '', '', '', ''))
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
    #< EVEN OUT FIGHTERS WITH REMAINING FIGHTERS
    for x in match_fighters:
        for y in x:
            total_match_fighters.append(y)
    remainder_fighters = []
    for af in list(fighters["FIGHTER_NAME"]):
        if af in total_match_fighters:
            continue
        else:
            remainder_fighters.append(af)
    total_number_of_players = len(named_found_fighters)
    total_smashdown_fights = fight_total[total_number_of_players]
    for x in final_dict['PLAYER'].values():
        while len(x['FIGHTERS']) > total_smashdown_fights:
            x['FIGHTERS'].remove(random.sample(x['FIGHTERS'], 1)[0])
        while len(x['FIGHTERS']) < total_smashdown_fights:
            added_fighter = random.sample(remainder_fighters, 1)[0]
            x['FIGHTERS'].append(added_fighter)
            remainder_fighters.remove(added_fighter)    
    return final_dict

# fight_setup(str.title('Sokol'),str.title('Reen'),str.title("Joe"),str.title("fart"))