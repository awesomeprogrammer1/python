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


while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Song database",
        ["Add Artist", "Add Song", "Save", "Load", "Exit"],
    )
    if interface == "Add Artist":
        # song_plays = {}
        # file_handle = open(file_path, "w")
        # artist_db = json.load(file_handle)
        add_artist = enterbox(
            "Please enter the name of a musical artist", "Add Artist"
        )
        song_plays[add_artist[1]] = add_artist[2]
        artist_db[song_plays] = add_artist[0]
