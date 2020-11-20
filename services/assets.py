from services.categories import get_price
from db.db import Session
from models import Asset


def _get_or_create_asset(session, category_id):
    asset = session.query(Asset).filter_by(category_id=category_id).first()
    if asset is not None:
        return asset
    asset = Asset(category_id=category_id, amount=0)
    session.add(asset)
    return asset


class NotEnoughAssetAmount(Exception):
    pass


def get_all_assets():
    session = Session()
    return session.query(Asset).all()


def update_amount(category_id, amount, delta):
    """Updates asset amount and returns the new amount"""
    session = Session()

    asset = _get_or_create_asset(
        session=session,
        category_id=category_id,
    )

    if delta:
        amount = asset.amount + amount
    if amount < 0:
        raise NotEnoughAssetAmount()
    asset.amount = amount
    if asset.amount == 0:
        session.delete(asset)
    session.commit()


def calculate_worth(asset):
    return get_price(asset.category)
