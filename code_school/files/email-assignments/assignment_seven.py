'''
Task 7
You have an array of strings.
Write them to a file while placing each array element
on a separate line and preserving the order.
'''
import os.path
from pathlib import Path

path_write = Path("code_school\\files\work_files")

basic_write = path_write / "test1.txt"

write_in_file = open(basic_write, "w")

array_of_strings = ["str1", "str2", "str3"]
seperate_lines = "\n".join(array_of_strings)
write_in_file.write(seperate_lines)
write_in_file.close()
