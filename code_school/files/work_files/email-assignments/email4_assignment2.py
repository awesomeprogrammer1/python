'''
Task 2:
There is a dictionary that stores the name of bands
(singers) and their albums. Implement the following
Adding, deleting, finding, editing, saving, and loading data
(Use packing and unpacking)
'''
from pathlib import Path
from easygui import *
import json


folder_with_info = Path("code_school/files/work_files")
file_path = folder_with_info / "email4_assignment2_output.json"
artist_songs = {}

while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Song database",
        ["Add Artist", "Add Song", "Save", "Load", "Exit"],
    )
    if interface == "Add Artist":
        file_load = open(file_path, "r")
        artist_db = json.load(file_load)
        file_handle = open(file_path, "w")
        add_artist = enterbox(
            "Please enter the name of a musical artist", "Add Artist"
        )
        if add_artist in file_load.keys():
            textbox("Error: Artist already exists")
        file_load[add_artist] = {}
        json.dump(file_load)
        textbox(file_load)
        file_load.close()
        file_handle.close()
        if interface == "Add Song":
            file_load = open(file_path, "r")
            artist_db_s = json.load(file_load)
            file_handle = open(file_path, "w")
            current_song_plays = {}
            check_artist = enterbox(
                "Please enter the name of a musical artist to add a song to", "Add Song"
            )
            if check_artist not in file_load.keys():
                textbox("Error, Artist Doesn't Exist")
            song_and_plays = multenterbox(
                "Please enter the song with the plays ", "Add Song", ["Song", "Song Listens"]
                )
            current_song_info = {}
            current_song_info[song_and_plays[0]] = song_and_plays[1]
            file_load[check_artist][song_and_plays[0]] = song_and_plays[1]
            json.dump(file_load)
            file_load.close()
            file_handle.close()






        
