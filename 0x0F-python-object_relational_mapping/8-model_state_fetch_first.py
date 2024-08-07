#!/usr/bin/python3

"""
prints the first State object
from the database hbtn_0e_6_usa
"""

from sys import argv, exit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access the database and retrieve the first state
    """

    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print("Nothing")
