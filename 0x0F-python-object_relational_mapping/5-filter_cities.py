#!/usr/bin/python3
"""Lists all cities from a databases that match argument"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    passwd = argv[2]
    dbname = argv[3]
    sname = argv[4]
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=passwd,
                               db=dbname)

    cur = database.cursor()
    cur.execute(
        "SELECT cities.name FROM cities \
        INNER JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s;", (sname,))
    rows = cur.fetchall()
    s = []
    for row in rows:
        s.append(row[0])
    print(', '.join(s))
    cur.close()
    database.close()
