from db.db import Session
from models import Category
from services.trackers import ALL_TRACKERS


class NoTrackerError(Exception):
    pass


def _get_tracker(category):
    print(category.name)
    if category.name not in ALL_TRACKERS:
        raise NoTrackerError()
    return ALL_TRACKERS[category.name]


def get_all_categories():
    session = Session()
    return session.query(Category).all()


def get_price(category):
    """Returns current price of category"""
    tracker = _get_tracker(category)
    return tracker.get_price()
