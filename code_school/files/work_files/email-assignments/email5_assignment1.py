import os.path

path1 = os.path.join("code_school\files\work_files", "email5_assignment1_input.txt")
path2 = os.path.join("code_school\\files\work_files", "email5_assignment1_bad_words.txt")
path3 = os.path.join("code_school\\files\work_files", "email5_assignment1_output.txt")

sample_text = open(path1, "r")
bad_words_file = open(path2, "r")
output_text = open(path3, "w")

original_text = sample_text.read()
bad_words = bad_words_file.read().split()

for word in bad_words:
    if word in original_text:
        output = original_text.replace(word,'')
output_text.write(output_text)
sample_text.close()
bad_words_file.close()
output_text.close()