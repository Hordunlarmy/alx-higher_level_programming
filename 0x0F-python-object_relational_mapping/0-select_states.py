#!/usr/bin/python3
# a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],  passwd=sys.argv[2],
        db=sys.argv[3])

    db = db.cursor()

    db.execute("SELECT * FROM states")

    rows = db.fetchall()

    for row in rows:
        print(row)
