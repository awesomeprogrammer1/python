import os.path

path = os.path.join("code_school\\files\work_files", "test1.txt")

file_obj = open(path, "w")
file_obj.write("Hello")
# file_obj.close()
