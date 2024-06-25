#!/usr/bin/python3
"""
Prints the first State object from the database
hbtn_0e_6_usa where the name contains 'a'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create the database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all tables defined in the models
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object where name contains 'a'
    state = session.query(State).filter(State.name.like('%a%')).first()

    # Check if a state was found
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
