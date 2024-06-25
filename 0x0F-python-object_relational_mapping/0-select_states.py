#!/usr/bin/python3

"""
lists all states from the database htbn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Get MySQL credentials and database name
    from command line arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """let's connect to MySQL server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
