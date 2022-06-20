size = int(input("Input size for multiplication table "))
Counter = 1
while size+1 > Counter:
    Number=Counter
    while Number<= size * Counter:
        print(Number, end='\t')
        Number +=Counter
    print()
    Counter+=1