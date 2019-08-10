#!/usr/bin/python3
"""Module to fetch the first state in a table"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = session.query(State).first()

    if state_name.id is not None:
        print("{}: {}".format(state_name.id, state_name.name))
    else:
        print("Nothing")
