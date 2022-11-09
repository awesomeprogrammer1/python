'''
Get two files
Write common words to the third file
'''
import os.path
from pathlib import Path
folder_with_info = Path("code_school/files/work_files")
file1_path = folder_with_info / "email5_assignment4_text.txt"
file2_path = folder_with_info / "email5_assignment4_text2.txt"
file1_handle = open(file1_path, "r")
file2_handle = open(file2_path, "r")
file1_words = file1_handle.read().split()
file2 = file2_handle.read().lower().split()
file1_handle.close()
file2_handle.close()
output_list = []
for word in file1_words:
    if word.lower() in file2:
        output_list.append(word.lower())
output_list_set = set(output_list)
common_words = "\n".join(output_list_set)
folder_with_info = Path("code_school/files/work_files")
file3_path = folder_with_info / "email5_assignment4_output.txt"
write_words = open(file3_path, "w")
write_words.write(common_words)
write_words.close()
