# coding=utf-8
# !/usr/bin/python3

import requests

from keys.keys import OMBD_KEY


class OMDb:

    def __init__(self) -> None:
        super().__init__()
        self.BASE_URL = "http://www.omdbapi.com/"

    def search_media(self, media_id):
        r = requests.get(f"{self.BASE_URL}?i={media_id}&apikey={OMBD_KEY}")
        if r.status_code == 200:
            print(r.json())

# TEST
# if __name__ == '__main__':
#     OMDb().search_media("tt1179056")
