word = input("Enter a name: ")
word_dict = {word: {character: word.count(character) for character in word}}
print(word_dict)
