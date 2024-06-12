import pandas as pd

fighters = pd.read_csv('WhiskeySmash/CSV/FIGHTER_202406042059.csv')

def createGrid():
    home_grid = {'FIRST_ROW':[], "SECOND_ROW":[], 'THIRD_ROW':[], 'FOURTH_ROW':[], 'FIFTH_ROW':[], "SIXTH_ROW":[],'SEVENTH_ROW':[]}
    for x in range(0, 13):
        home_grid["FIRST_ROW"].append(fighters['FIGHTER_NAME'][x])
    for x in range(13, 26):
        home_grid["SECOND_ROW"].append(fighters['FIGHTER_NAME'][x])
    for x in range(26, 39):
        home_grid["THIRD_ROW"].append(fighters['FIGHTER_NAME'][x])
    for x in range(39, 52):
        home_grid["FOURTH_ROW"].append(fighters['FIGHTER_NAME'][x])
    for x in range(52, 65):
        home_grid["FIFTH_ROW"].append(fighters['FIGHTER_NAME'][x])
    for x in range(65, 78):
        home_grid["SIXTH_ROW"].append(fighters['FIGHTER_NAME'][x])
    for x in range(78, 83):
        home_grid["SEVENTH_ROW"].append(fighters['FIGHTER_NAME'][x])
    return home_grid