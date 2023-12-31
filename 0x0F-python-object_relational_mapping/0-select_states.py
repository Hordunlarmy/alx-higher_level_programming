#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database and retrieve data
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
