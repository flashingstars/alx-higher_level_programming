#!/usr/bin/python3
""" slqalchmy query """

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine, join


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).join(State)
    results = query.all()
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
