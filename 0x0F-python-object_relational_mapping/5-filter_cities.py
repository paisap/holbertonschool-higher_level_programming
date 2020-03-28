#!/usr/bin/python3
""" All cities by state  """
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    state = sys.argv[4]
    query = "SELECT c.name FROM cities c INNER JOIN states s \
                    ON c.state_id = s.id WHERE s.name = %s ORDER BY c.id ASC"
    cur.execute(query, (state,))
    query_rows = cur.fetchall()
    aux = []
    for i in query_rows:
        aux.append(i[0])
    print(', '.join(aux))
    cur.close()
    conn.close()
