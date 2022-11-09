'''
Task 9 You have a text file. Calculate the number of characters in it.
'''
import os.path


path_read = os.path.join("code_school\\files\work_files", "assignment1.txt")

file = open(path_read, "r")

characters_in_file = file.read()
print(f"Characters in the file: {len(characters_in_file)}")
file.close()
