import os
from argparse import ArgumentParser

from db import init as db_init
from settings import DB_URL


def init_db():
    db_init.init_db()
    db_init.populate_db()


def remove_db():
    db_path = DB_URL.split('///')[1]
    os.remove(db_path)


if __name__ == '__main__':
    parser = ArgumentParser(description='Manage app')
    subparsers = parser.add_subparsers(dest='service')

    db_parser = subparsers.add_parser('db')
    db_subparsers = db_parser.add_subparsers(dest='command')
    init_db_parser = db_subparsers.add_parser('init')
    remove_db_parser = db_subparsers.add_parser('remove')

    args = parser.parse_args()

    if args.service == 'db':
        if args.command == 'init':
            init_db()
        elif args.command == 'remove':
            remove_db()

    print("Done.")
