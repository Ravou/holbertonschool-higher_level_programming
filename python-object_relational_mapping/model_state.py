#!/usr/bin/python3
"""
Defines a State class and creates a Base instance
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

# Create the base class
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    name = Column(
        String(128),
        nullable=False
    )


# The following code is for testing purposes only
if __name__ == "__main__":
    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))

    # Create all tables in the engine
    Base.metadata.create_all(engine)
