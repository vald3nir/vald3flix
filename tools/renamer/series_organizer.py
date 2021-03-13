# coding=utf-8
import glob
import os
import re

folder_rename_series = '/media/vald3nir/Arquivos/Google Drive/Vald3flix/Séries/Wandavision'
series_name = "Wandavision"
season = "01"

flag_rename = True
flag_rename = False


# ------------------------------------------------------------------------------------

def rename_file(old_file, new_file):
    try:
        print('-------------------------------------------------------')
        print(old_file)
        print(new_file)
        if flag_rename and not os.path.exists(new_file):
            os.rename(old_file, new_file)
    except:
        print("Erro", old_file, new_file)


# ------------------------------------------------------------------------------------


def rename_series():
    episodes = [f for f in glob.glob(folder_rename_series + "**/*.*", recursive=True)]

    def get_index_movie(index):
        if index < 10:
            return "0" + str(index)
        else:
            return str(index)

    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        return [atoi(c) for c in re.split('(\d+)', text)]

    episodes.sort(key=natural_keys)
    i = 1

    new_folder = os.path.join(folder_rename_series, series_name)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for episode in episodes:
        if not os.path.isdir(episode):
            extension = str(episode).split(".")
            extension = "." + str(extension[-1])

            episode_renamed = series_name + " - " + season + "x" + get_index_movie(i) + extension
            episode_renamed = os.path.join(new_folder, episode_renamed)

            rename_file(episode, episode_renamed)
            i += 1


# ------------------------------------------------------------------------------------

if __name__ == '__main__':
    rename_series()
    print("Game Over")
