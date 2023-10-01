'''
deletion of data present in the table.
'''
import sqlite3
from pprint import pprint

def delete(Database_Name):
    con = sqlite3.connect(Database_Name)
    con.execute('''DELETE FROM universities WHERE "Industry Income Score" < 90.0;''')
    
    cursor = con.execute('''SELECT "Name of University" FROM universities''')
    con.commit()

    results = cursor.fetchall()
    return pprint(results)