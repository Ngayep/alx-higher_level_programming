#!/usr/bin/python3

"""
Lists all values in the states tables
of a database where name
matches the argument
"""
import MySQLdb
from sys import argv, exit

if len(argv) != 5:
    print("Usage: ./2-my_filter_states.py <username> <password> "
          "<database> <search>")
    exit(1)

if __name__ == '__main__':
    try:
        # Connect to the database
        db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Prepare the SQL query
        query = ("SELECT * "
                 "FROM states "
                 "WHERE name LIKE BINARY %s "
                 "ORDER BY id ASC")

        # Execute the query
        cursor.execute(query, (argv[4],))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.OperationalError as e:
        print(f"Error: {e}")
        exit(1)
