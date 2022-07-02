inf=open('words.txt','r')
words_list = []
for i in inf:
    words_list.append(i.strip())
inf.close()
