import functools

from services.assets import calculate_worth, get_all_assets


def calculate_wealth() -> int:
    assets = get_all_assets()
    return functools.reduce(
        lambda a, b: a + b, map(lambda asset: calculate_worth(asset), assets), 0
    )
