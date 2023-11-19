#!/usr/bin/python3
"""
Start link class to table in the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    print("Connecting to the database...")
    try:
        connection = engine.connect()
        print("Connected successfully!")
        connection.close()
    except Exception as e:
        print("Error connecting to the database:", e)

    # Create tables
    Base.metadata.create_all(engine)
