"""
Task 8 You have an array of strings. 
Write them to a file while placing each array element on a 
separate line and reversing the order.
"""
import os.path
from pathlib import Path

path_write = Path("code_school\\files\work_files")

write_in_file = path_write / "test1.txt"
f_write = open(write_in_file, "w")

array_of_strings = ["str1", "str2", "str3"]
array_of_strings.reverse()
seperate_lines = "\n".join(array_of_strings)
f_write.write(seperate_lines)
f_write.close()
