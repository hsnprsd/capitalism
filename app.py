import logging

from flask import Flask, redirect, render_template, request

from services.assets import get_all_assets, calculate_worth, update_amount
from services.categories import get_all_categories, get_price
from services.wealth import calculate_wealth

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'current_wealth': calculate_wealth(),
    }
    return render_template('index.html', **context)


@app.route('/categories')
def categories():
    categories = get_all_categories()
    category_prices = {}
    for category in categories:
        try:
            price = get_price(category)
            category_prices[category.id] = price
        except Exception as e:
            logger.error(e)
            raise
    context = {
        'categories': categories,
        'category_prices': category_prices,
    }
    return render_template('categories.html', **context)


@app.route('/assets')
def assets():
    assets = get_all_assets()
    asset_worths = {}
    for asset in assets:
        asset_worths[asset.id] = calculate_worth(asset)
    context = {
        'categories': get_all_categories(),
        'assets': assets,
        'asset_worths': asset_worths,
    }
    return render_template('assets.html', **context)


@app.route('/assets/update', methods=['POST'])
def update_assets():
    data = request.form
    if 'category_id' not in data:
        return "Bad request", 400
    update_amount(
        category_id=int(data['category_id']),
        amount=int(data.get('amount', 0)),
        delta=bool(data.get('delta', True)),
    )
    return redirect(location='/assets')
