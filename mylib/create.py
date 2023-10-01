import sqlite3
import pandas as pd

con = sqlite3.connect('ranking.db')
wb = pd.read_csv('World University Rankings 2023.csv',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()