"""
Add the nobel-prize dataset to a sqlite database
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from nobel import NOBEL_WINNERS

Base = declarative_base()


class Winner(Base):
    """
    Object for the winners table of the database
    """

    __tablename__ = "winners"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum("male", "female"))

    def __repr__(self):
        return "<Winner(name='{}', category='{}', year='{}')>".format(
            self.name, self.category, self.year
        )


def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop("id")
    return dat


def populate(session, data):
    winner_rows = [Winner(**w) for w in data]
    session.add_all(winner_rows)
    session.commit()


def nobel_summary(session):
    # How many winners are in the database?
    print(session.query(Winner).count())

    # All Swiss winners
    result = session.query(Winner).filter_by(nationality="Swiss")
    print(list(result))

    # All non-Swiss Physics winners
    result = session.query(Winner).filter(
        Winner.category == "Physics", Winner.nationality != "Swiss"
    )
    print(list(result))

    # The third entry
    print(session.query(Winner).get(3))

    # Winners ordered by year
    result = session.query(Winner).order_by("year")
    print(list(result))

    # Winners converted back to dictionaries
    winner_rows = session.query(Winner)
    nobel_winners = [inst_to_dict(w) for w in winner_rows]
    print(nobel_winners)


def destructive_updates(session, engine):
    # Update Marie Curie's nationality to French
    marie = session.query(Winner).get(3)
    marie.nationality = "French"
    print(session.dirty)
    session.commit()
    print(session.dirty)
    print(session.query(Winner).get(3).nationality)

    # Delete Albert Einstein's entry
    session.query(Winner).filter_by(name="Albert Einstein").delete()
    session.commit()
    print(list(session.query(Winner)))

    # Drop the whole table
    Winner.__table__.drop(engine)


if __name__ == "__main__":
    URL = "sqlite:///data/nobel_prize.db"
    ENGINE = create_engine(URL, echo=True)
    Base.metadata.create_all(ENGINE)
    SESSION = sessionmaker(bind=ENGINE)()
    populate(SESSION, NOBEL_WINNERS)
    nobel_summary(SESSION)

    # destructive_updates(SESSION, ENGINE)
