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
        return r.json()

    def search_medias(self, media_ids):
        medias = []
        index = 1
        size = len(media_ids)
        for media_id in media_ids:
            print(f"id {index}/{size}: {media_id}")
            medias.append(self.search_media(media_id=media_id))
            index += 1
        return medias

# TEST
# if __name__ == '__main__':
#     # print(OMDb().search_media("tt1179056"))
#     print(OMDb().search_medias(["tt1014763", "tt1259521"]))
