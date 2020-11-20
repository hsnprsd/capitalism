from db.db import Base, engine, Session
from models import Category


def init_db():
    # noinspection PyUnresolvedReferences
    import models
    Base.metadata.create_all(engine)


def populate_db():
    session = Session()

    categories = [
        'gold',
        'toman',
    ]
    session.add_all([Category(name=name) for name in categories])

    session.commit()
