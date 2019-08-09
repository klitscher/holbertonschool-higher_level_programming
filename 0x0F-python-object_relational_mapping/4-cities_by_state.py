#!/usr/bin/python3
"""Lists all cities from a databases"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    passwd = argv[2]
    dbname = argv[3]
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=passwd,
                               db=dbname)

    cur = database.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states ON states.id = cities.state_id \
        ORDER BY cities.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
