#!/usr/bin/python3
"""Script to lists all states form a database"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
        username = argv[1]
        passwd = argv[2]
        dbname = argv[3]

        database = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=passwd, db=dbname)
        cur = database.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()

        for row in rows:
            print("{}".format(row))

        cur.close()
        database.close()
