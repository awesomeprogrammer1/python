import os.path


path_read = os.path.join("code_school\\files\work_files", "assignment1.txt")

file = open(path_read, "r")

characters_in_file = file.read()
print(len(characters_in_file))
file.close()
