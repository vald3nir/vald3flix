# coding=utf-8

import os
import xml.etree.ElementTree as ET

# ------------------------------------------------------------------------------------

movies_folder = '/media/vald3nir/Arquivos/Vald3flix/Filmes'

flag_rename = True
flag_rename = False


# ------------------------------------------------------------------------------------

def rename_file(old_file, new_file):
    try:
        print('-------------------------------------------------------')
        print(" * ", old_file)
        print("-> ", new_file)
        if flag_rename and not os.path.exists(new_file):
            os.rename(old_file, new_file)
    except:
        print("Erro", old_file, new_file)


def format_movie_title(tittle):
    return tittle.replace(":", " -").replace("As ", "").replace("A ", "").replace("Os ", "").replace("O ", "")


def generate_movie_name(file_nfo):
    for element in ET.parse(file_nfo).getroot().iter('movie'):
        movie_name = '{title} - ({year}) [{imdbid}]'
        _year = '2020'

        for n in range(len(element)):
            tag = '{0}'.format(element[n].tag)

            if tag == 'year':
                _year = '{0}'.format(element[n].text)
                movie_name = movie_name.replace('{year}', _year)

            if tag == 'title':
                movie_name = movie_name.replace('{title}', '{0}'.format(format_movie_title(element[n].text)))

            if tag == 'imdbid':
                movie_name = movie_name.replace('{imdbid}', '{0}'.format(element[n].text))

        return os.path.join(movies_folder, movie_name)


def rename_movies():
    files_nfo = []
    for root, dirs, files in os.walk(movies_folder):
        for file in files:
            if file.endswith('.nfo'):
                files_nfo.append(os.path.join(root, file))

    for file_nfo in files_nfo:
        old_movie = str(file_nfo).replace('.nfo', '')
        new_movie = generate_movie_name(file_nfo)

        if old_movie != new_movie:
            for extension in [".mp4", ".avi", ".mkv", ".srt", ".nfo"]:
                if os.path.exists(old_movie + extension):
                    rename_file(old_movie + extension, new_movie + extension)


# ------------------------------------------------------------------------------------

if __name__ == '__main__':
    rename_movies()
    print("Game Over")
