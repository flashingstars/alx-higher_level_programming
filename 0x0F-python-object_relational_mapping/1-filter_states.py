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
    cur = connection.cursor()
    try:
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("execution failed")
    cur.close()
    connection.close()
