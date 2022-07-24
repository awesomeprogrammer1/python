# assignment 1
# castle = [1, ["c"], 543, "P", ["e"], ["n", ["r"]], "i", [[["s"]]]]
# a = "" + castle[3] + castle[]
# assignment 2
# make sure that the menu in contact_book reappears
# after every operation
# additionally, add an 'exit' button
# and implement all the other buttons
# assignment 3
# message = [("We ",),"rec",{"r":"o"},{"o":"r"},{"m1":"ded "},{"m3":["a "], "m4":{"m5": "UFO"}}]
# Feel like a hacker. Go through all the levels of protection, and decode the secret message of the secret services. Intercepted message


# dict = {}

# sentence1_words = input("Enter a sentence: ").split()  # ["1 word", "2 word", "3 word"]
# sentence2_words = input(
#     "Enter a sentence with the same amount of words as the first one: "
# ).split()


# if len(sentence1_words) != len(sentence2_words):
#     print("Error")
# else:
#     for i in range(len(sentence1_words)):

#         # if sentence1_words[i] in dict.keys():
#         #     dict[sentence1_words[i]] =  dict[sentence1_words[i]] + ", " + sentence2_words[i]
#         #

#         # list = []
#         # list.append(sentence2_words[i])
#         # dict[sentence1_words[i]] = list

#         # conditional operator checks if the word in the sentence is repeating
#         if sentence1_words[i] in dict.keys():
#             # create an empty list
#             list = []
#             # adding the value in the first element that the word appears
#             list.append(dict[sentence1_words[i]])
#             # adding the value in the second element that the word appears in
#             list.append(sentence2_words[i])
#             # adds the key 'dad' back under the values in the list
#             dict[sentence1_words[i]] = list
#         else:
#             # adds the element to the dictionary
#             dict[sentence1_words[i]] = sentence2_words[i]

#     print(dict)

# list = [['love', 'very'], 'too']
# print(list[1])
# print(list[0])
# print(list[0][0])
#


castle = [1, ["c"], 543, "P", ["e"], ["n", ["r"]], "i", [[["s"]]]]
print(castle)
a = (
    ""
    + castle[3]
    + castle[5][1][0]
    + castle[6]
    + castle[5][0]
    + castle[1][0]
    + castle[4][0]
    + castle[7][0][0][0][0]
    + castle[7][0][0][0][0]
)
print(a)
