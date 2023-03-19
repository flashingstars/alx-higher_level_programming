#!/usr/bin/python3
""" selecting with mysqldb """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("error connecting")
    try:
        cur = connection.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("execution failed")
    cur.close()
    connection.close()
