import requests
from bs4 import BeautifulSoup

from services.trackers.exceptions import UnknownPrice


def get_price() -> float:
    link = 'https://www.tgju.org/profile/mesghal'
    response = requests.get(link)
    if response.status_code != 200:
        raise UnknownPrice()

    soup = BeautifulSoup(response.content, features='html.parser')
    table = soup.find(lambda tag: tag.name == 'table')
    tbody = table.find(lambda tag: tag.name == 'tbody')
    rows = tbody.find_all(lambda tag: tag.name == 'tr')
    current_price_row = rows[0]
    current_price = current_price_row.find_all(lambda tag: tag.name == 'td')[1].text
    return int(current_price.replace(',', '')) / 10
