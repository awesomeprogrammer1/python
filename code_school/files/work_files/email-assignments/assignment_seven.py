'''
Task 7
You have an array of strings. 
Write them to a file while placing each array element 
on a separate line and preserving the order.
'''
import os.path

path_write = os.path.join("code_school\\files\work_files", "test1.txt")

write_in_file = open(path_write, "w")

array_of_strings = ["str1", "str2", "str3"]
seperate_lines = "\n".join(array_of_strings)
write_in_file.write(seperate_lines)
write_in_file.close()
