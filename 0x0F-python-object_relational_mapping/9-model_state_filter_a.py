#!/usr/bin/python3
"""
Prints the first State object from the database
hbtn_0e_6_usa where the name contains 'a'.
"""
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv, exit

if __name__ == "__main__":
 
    if len(argv) != 4:
        print("Usage: ./7.py <username> <password> <database>")
        exit(1)

    usr, passwd, db = argv[1], argv[2], argv[3]

    eng = "mysql://" + usr + ":" + passwd + "@localhost:3306/" + db
    try:
        engine = sqlalchemy.create_engine(eng)
    except Exception as err:
        print(err)
        exit(1)
    Session = sessionmaker(bind=engine)
    session = Session()
    for rows in session.query(State).filter(State.name.like('%a%')):
        print("{:d}: {:s}".format(rows.id, rows.name))
    session.close()
