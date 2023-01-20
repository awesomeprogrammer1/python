# Expected input + output:
# andrew is good boy  | {'andrew': {'a':1,'n':1...} , 'is': {'i':1,'s':1},...}
sentence = input("Enter a sentence: ").split()
word_dict = {sentence[i]: {character: sentence[i].count(character) for character in sentence[i]} for i in range(len(sentence))}
print(word_dict)
