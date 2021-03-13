# coding=utf-8

import os

movies_folder = "/media/vald3nir/Arquivos/Vald3flix/Filmes"

ids = {""}
ids.clear()

for root, dirs, files in os.walk(movies_folder):
    for s in files:
        ids.add("tt" + s[s.find('[tt') + len('[tt'):s.rfind(']')])

with open('ids.txt', 'w') as file:
    for key in ids:
        file.write(f"{key}\n")

print(f"{len(ids)} Movies")
