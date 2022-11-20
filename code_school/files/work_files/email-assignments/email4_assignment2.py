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

while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Song database",
        ["Add Artist", "Add Song", "Delete Artist", "Delete Song", "Edit Song", "Exit"],
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
    elif interface == "Add Song":
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
            current_song_info[song_info[0]] = song_info[1]
            artist_db[artist_name][song_info[0]] = song_info[1]
            file = open(file_path, "w")
            json.dump(artist_db, file)
            file.close()
    elif interface == "Delete Artist":
        file = open(file_path, "r")
        artist_db = json.load(file)
        file.close()
        artist_name = enterbox("Please enter the name of the musical artist", "Delete Artist")
        if artist_name not in artist_db.keys():
            textbox("Error: Artist does not exist")
        else:
            artist_db.pop(artist_name)
        file = open(file_path, "w")
        json.dump(artist_db, file)
        file.close()
    elif interface == "Delete Song":
        file = open(file_path, "r")
        artist_db = json.load(file)
        file.close()
        artist_name = enterbox("Please enter the name of a musical artist", "Delete Song")
        if artist_name not in artist_db:
            textbox("Error: Artist does not exist.")
        else:
            song_name = enterbox("Enter the name of the song you would like to delete", "Delete Song")
            if song_name not in artist_db[artist_name]:
                textbox("Error: Song does not exist.")
            else:
                artist_db[artist_name].pop(song_name)
                file = open(file_path, "w")
                json.dump(artist_db, file)
                file.close()
    elif interface == "Edit Song":
        file = open(file_path, "r")
        artist_db = json.load(file)
        file.close()
        song_info = multenterbox(
                "Enter Song Information",
                "Edit Song",
                ["Artist Name", "Song Name"],
            )
        if song_info[0] not in artist_db:
            textbox("Error, artist doesnt exist.")
        else:
            if song_info[1] not in artist_db[song_info[0]]:
                textbox("Error, song doesnt exist.")
            else:
                edit_plays = enterbox("Please enter the new number of plays", "Edit Song Plays")
                artist_db[song_info[0]][song_info[1]] = edit_plays
                file = open(file_path, "w")
                json.dump(artist_db, file)
                file.close()
    if interface == "Exit":
        break
