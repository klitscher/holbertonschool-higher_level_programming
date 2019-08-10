#!/usr/bin/python3
"""Script to filter states"""


from sys import argv
import MySQLdb


def main():
    """Main function"""

    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=dbname)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name \
    LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()

if __name__ == '__main__':
    main()
