# coding=utf-8
# !/usr/bin/python3

import pymongo

from keys.keys import *

# collections:
MOVIES = "movies"
SERIES = "series"

# DB CONFIG
DATABASE = "vald3flix"
USER = DB_USER_NAME
PASSWORD = DB_USER_PASSWORD


class DatabaseHandler:

    def __init__(self) -> None:
        super().__init__()
        client = pymongo.MongoClient(
            f"mongodb+srv://{USER}:{PASSWORD}@realmcluster.ikdg6.mongodb.net/{DATABASE}?retryWrites=true&w=majority")
        self.db = client[DATABASE]

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def update(self, collection, query, new_value):
        self.db[collection].update_one(query, new_value, upsert=True)

    def insert_one(self, collection, query):
        self.db[collection].insert_one(query)

    def find_all(self, collection, query=None):
        if query is None:
            query = {}
        return list(self.db[collection].find(query))

    def clear(self, collection):
        self.db[collection].drop()
