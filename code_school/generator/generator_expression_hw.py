sentence = input("Enter a sentence: ").split()
word_dict = {sentence[i]: {character: sentence[i].count(character) for character in sentence[i]} for i in range(len(sentence))}
print(word_dict)
