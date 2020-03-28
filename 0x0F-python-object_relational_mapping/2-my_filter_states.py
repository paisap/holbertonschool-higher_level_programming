#!/usr/bin/python3
""" Filter states """
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE {} ORDER BY id ASC;"
    y = sys.argv[4]
    cur.execute(query, (y,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
