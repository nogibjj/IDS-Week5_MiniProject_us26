'''
Reading data from a database
'''

import sqlite3
from pprint import pprint

def read(Database_Name):
    cnt = sqlite3.connect(Database_Name)

    print('Name of university in USA :')
    
    cursor = cnt.execute('''SELECT "Name of University" FROM universities WHERE
                        "Location" == "United States";''')
      
    pprint(cursor)
    print('')  # Print new line
    
    print('Name of University where No of student per staff is greater than 40.0')
    
    cursor = cnt.execute('''SELECT "Name of University", "No of student per staff" FROM
    universities WHERE "No of student per staff">40.0;''')
    pprint(cursor)

    return
