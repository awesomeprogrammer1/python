import random

s= 'Section 1.10.33 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC'
alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in s:
    if i in alphabet:
     print(i,end=', ')
