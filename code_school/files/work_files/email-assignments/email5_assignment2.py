"""
Task 2 Write a Russian-English transliteration program.
Data for transliteration are taken from a file and written to another file.
The direction is chosen by the user through a menu.
"""
import os.path
from easygui import *
translated_words = ""
russian_words = os.path.join("code_school\\files\work_files", "russian_words.txt")
read_words = open(russian_words, "r", encoding="utf8")
russian_words = read_words.read().split()
for word in russian_words:
    english_word = enterbox(
            f"Enter translation for {word}",
            "Translate Text"
        )
    translated_words += english_word
    translated_words += ' '
transliterated_words = os.path.join("code_school\\files\work_files", "transliterated_words.txt")
write_words = open(transliterated_words, "w", encoding="utf8")
write_words.write(translated_words)
write_words.close()



