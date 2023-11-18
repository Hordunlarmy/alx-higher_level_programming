#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
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
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id", {'name': sys.argv[4]})

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
