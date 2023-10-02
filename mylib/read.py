"""
Reading data from a database
"""

import sqlite3
from pprint import pprint


def read(database_name):
    cnt = sqlite3.connect(database_name)

    print("Name of university in USA :")

    cursor = cnt.execute(
        """SELECT "Name of University" FROM universities WHERE
                        "Location" == "United States";"""
    )

    result = cursor.fetchall()
    pprint(result)
    print("")  # Print new line

    print("Name of University where No of student per staff is less than 40.0")

    cursor = cnt.execute(
        """SELECT "Name of University", "No of student per staff" FROM
    universities WHERE "No of student per staff"<40.0;"""
    )
    result = cursor.fetchall()
    pprint(result)

    print("")

    cursor = cnt.execute(
        """SELECT "Name of University", "No of student per staff" FROM
universities WHERE ("No of student per staff" < 40.0) OR ("Location" == "Canada");"""
    )
    result = cursor.fetchall()
    pprint(result)

    return
