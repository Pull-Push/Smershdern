import pandas as pd

ssb = pd.read_csv('SSBUltimate.csv')
for x in ssb.SERIES:
    print(x)