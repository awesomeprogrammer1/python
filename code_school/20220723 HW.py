dict = {}

sentence1_words = input("Enter a sentence: ").split()
sentence2_words = input("Enter a sentence with the same amount of words as the first one: ").split()
list = []


if len(sentence1_words) != len(sentence2_words):
    print("Error")
    exit()
for i in range(len(sentence1_words)):
    list.append(sentence1_words[i])
    if sentence1_words[i] in dict.keys():
        
        dict[sentence1_words[i]] = [dict[list]]
    else:
        dict[sentence1_words[i]] = sentence2_words[i]
print(dict)
