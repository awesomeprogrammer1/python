# assignment 1

dict = {}

sentence1_words = input("Enter a sentence: ").split()
sentence2_words = input(
    "Enter a sentence with the same amount of words as the first one: "
).split()
extra_words = []


if len(sentence1_words) != len(sentence2_words):
    print("Error")
    exit()
for i in range(len(sentence1_words)):
    extra_words = []
    extra_words.append(sentence1_words)
    extra_words.append(sentence2_words)
    
    dict[sentence1_words[i]] = extra_words
print(dict)


# assignment 2
