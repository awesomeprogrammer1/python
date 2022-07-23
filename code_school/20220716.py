dict = {}
dict2 = {}
sentence = 'I love sharkie'
sentence_words = sentence.split()
print(len(sentence_words))
for i in range(len(sentence_words)):
    print(sentence_words[i])
    dict[sentence_words[i]] = len(sentence_words[i])
print(dict)

for word in sentence_words:
    print(word)
#     print(sentence_words[i])
#     dict[sentence_words[i]] = len(sentence_words[i])
# print(dict)