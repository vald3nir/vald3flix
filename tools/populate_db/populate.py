# coding=utf-8
# !/usr/bin/python3

from apis.OMDb import OMDb
from db.database_handler import DatabaseHandler, MOVIES

db = DatabaseHandler()
db.clear(MOVIES)

api = OMDb()

with open('../ids_extractor/ids.txt', "r") as fd:
    movies_id = fd.read().splitlines()

movies = api.search_medias(movies_id)

for movie in movies:
    db.insert_one(MOVIES, movie)

print("Game Over")
