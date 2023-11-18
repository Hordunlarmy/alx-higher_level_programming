#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.id, cities.name FROM cities JOIN states \
            ON cities.state_id=states.id WHERE states.name LIKE BINARY \
            %(name)s ORDER BY cities.id", {'name': sys.argv[4]})

    rows = cursor.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    cursor.close()
    db.close()
