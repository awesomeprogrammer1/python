

# assignment 1: ask the user for two words of the same length.
# create a dictionary where the keys are the letters from the first word 
# and the values are the letters of the second word
# assignment 2: ask the user to enter two sentences
# each sentence has the same number of words
# create a dictionary where the keys are the words from the first sentence
# and the values are the words from the second sentence
# hint: use the split method
# assignment 3: ask three users for their names
# and ask them for their emails and phone numbers {"Admin": {"email":"admin@gmail.com", "phone": "+1111111"}}



# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# dict = {}

# for i in range(len(b)):   
#     dict[a[i]] = b[i] 
# print(dict)

# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
# print(b[4])

dict = {} #{"Andry": ["ball", "stick", "laptop"], "Sergey": ["1", "2","3"],}


for i in range(3):
    name = input('What is your name? ')
    # list = [easygui.enterbox('1 '), easygui.enterbox('2 '), easygui.enterbox('3 ')]
    # list = easygui.multenterbox("Enter your items","Game", ["1 item", "2 item", "3 item"])
    # list = []
    # for i in range(3):
    #     item   = easygui.enterbox('What do you need? ')
    #     list.append(item)
    dict[name] = list
print(dict)
        



