import os.path
from pathlib import Path

path1 = os.path.join("code_school\\files\work_files", "email5_assignment1_input.txt")
path2 = os.path.join(
    "code_school\\files\work_files", "email5_assignment1_bad_words.txt"
)
path3 = os.path.join("code_school\\files\work_files", "email5_assignment1_output.txt")

sample_text = open(path1, "r")
bad_words_file = open(path2, "r")
output_text = open(path3, "w")

original_text = sample_text.read().split()
bad_words = bad_words_file.read().split()

for word in original_text:
    if word in bad_words:
        original_text[original_text.index(word)] = ""
new_text = " ".join(original_text)
output_text.write(new_text)
sample_text.close()
bad_words_file.close()
output_text.close()
