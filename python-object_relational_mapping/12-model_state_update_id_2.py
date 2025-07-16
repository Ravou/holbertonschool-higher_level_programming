#!/usr/bin/python3
"""
Script that changes the name of a State object where id=2 to "New Mexico"
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    # Create engine and connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    try:
        # Find the state with id = 2
        state = session.query(State).filter(State.id == 2).first()

        if state:
            # Update the state name
            state.name = "New Mexico"
            session.commit()
        # No output needed as per requirements
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the session
        session.close()
