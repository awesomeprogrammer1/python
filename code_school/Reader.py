alphabet = 'abcdefghijklmnopqrstuvwxyz'


for letter in alphabet:
    inf=open('ReaderInput.txt','r')
    counter=0
    for i in inf:
        counter+=i.count(letter)
        counter+=i.count(letter.upper())
    print(letter.upper(),'  ',counter)
    inf.close()

