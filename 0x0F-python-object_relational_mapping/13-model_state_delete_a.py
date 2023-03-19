#!/usr/bin/python3
""" slqalchmy query """

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)
    results = query.all()
    for state in results:
        session.delete(state)
    session.commit()
    session.close()
