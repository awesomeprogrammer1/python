import os.path
from pathlib import Path

folder_with_info = Path("code_school/files/work_files")

file_open = folder_with_info / "pathlib_example.txt"

f_example = open(file_open, "w")
f_example.write("Now, this code can be run on a mac and a windows system!")
f_example.close()
