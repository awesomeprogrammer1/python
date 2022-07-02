a = int(input('What will be the minumum number on the x coordinate '))
b = int(input('What will be the maximum number on the x coordinate? '))
c = int(input('What will be the minumum number on the y coordinate? '))
d = int(input('What will be the maximum number of the y coordinate? ')) 

for i in range (a, b+1):
    print("\t", i, end='')
print()

for i in range (c, d+1):
    print(i, end=' \t ')  


    for j in range (a, b+1):
        print(i*j, end=' \t ')
    print()