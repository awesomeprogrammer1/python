# assignment 1


dict = {}

sentence1_words = input("Enter a sentence: ").split()  # ["1 word", "2 word", "3 word"]
sentence2_words = input(
    "Enter a sentence with the same amount of words as the first one: "
).split()


if len(sentence1_words) != len(sentence2_words):
    print("Error")
else:
    for i in range(len(sentence1_words)):
        # if sentence1_words[i] in dict.keys():
        #     dict[sentence1_words[i]] =  dict[sentence1_words[i]] + ", " + sentence2_words[i]
        #

        # list = []
        # list.append(sentence2_words[i])
        # dict[sentence1_words[i]] = list

        if sentence1_words[i] in dict.keys():
            list = []
            list.append(dict[sentence1_words[i]])
            list.append(sentence2_words[i])
            dict[sentence1_words[i]] = list
        else:
            dict[sentence1_words[i]] = sentence2_words[i]

    print(dict)

#
