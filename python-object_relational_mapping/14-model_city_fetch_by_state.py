#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
        # Query all cities with their corresponding state names
        cities = session.query(City, State)\
                      .join(State, City.state_id == State.id)\
                      .order_by(City.id)\
                      .all()

        # Print results in the required format
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    except Exception as e:
        print("Error:", e)
    finally:
        # Close the session
        session.close()
