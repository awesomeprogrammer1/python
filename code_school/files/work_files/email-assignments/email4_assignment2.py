"""
Task 2:
There is a dictionary that stores the name of bands
(singers) and their albums. Implement the following
Adding, deleting, finding, editing, saving, and loading data
(Use packing and unpacking)
"""
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
        file = open(file_path, "r")
        artist_db = json.load(file)
        file.close()
        artist_name = enterbox(
            "Please enter the name of a musical artist", "Add Artist"
        )
        # artist_db = {"Andrew": {"Help":100, "Me": 132567}}
        # add_artist = "Andrew"
        if artist_name in artist_db.keys():
            textbox("Error: Artist already exists")
        else:
            artist_db[artist_name] = {}
        # artist_db = {"Andrew": {}}
        file = open(file_path, "w")
        json.dump(artist_db, file)
        file.close()
    if interface == "Add Song":
        file = open(file_path, "r")
        artist_db = json.load(file)
        file.close()
        artist_name = enterbox("Please enter the name of a musical artist", "Add Song")
        if artist_name not in artist_db.keys():
            textbox("Error: Artist does not exist")
        else:
            song_info = multenterbox(
                "Enter Song Information",
                "Add Song",
                ("Song Name", "Number of Plays"),
            )
            current_song_info = {}
            current_song_info[song_and_plays[0]] = song_and_plays[1]
            file_load[check_artist][song_and_plays[0]] = song_and_plays[1]
            json.dump(file_load)
            file_load.close()
            file_handle.close()
