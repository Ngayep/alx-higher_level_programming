#!/usr/bin/python3

"""
 takes in the name of a state as an argument
 and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db_connect.cursor()
    cursor.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities JOIN states
        ON
            cities.state_id = states.id
        WHERE
            states.name = '{}';""".format(argv[4]))

    rows = cursor.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
