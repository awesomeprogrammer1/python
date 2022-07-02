import random
from xml.dom import NotFoundErr
list_of_numbers = [random.randint(-100,100) for i in range(200)]
def minimum(my_list):
    smallest_number = my_list[0]
    for i in my_list:
        if smallest_number > i:
            smallest_number=i
    return smallest_number

def maximum(my_list):
    biggest_number = my_list[0]
    for i in my_list:
        if biggest_number < i:
            biggest_number=i
    return biggest_number

def search(my_list,x):
    count=0
    for i in range(len(my_list)):
        count+=1
        if x == my_list[i]:
            return (x,i,count)
    return NotFoundErr

def binary_search(my_list,x):
    #sorted(my_list)
    my_list=sorted(my_list)
    #print(my_list.index(x))
    Left=0
    Right=len(my_list)-1
    Middle=(Left+Right)//2
    Count=0
    while not (Left >= Right):
        Count+=1
        if my_list[Middle]==x:
            Left=Right
            return(x,Middle,Count)
        if my_list[Middle]<x:
            Left=Middle+1
        if my_list[Middle]>x:
            Right=Middle-1
        Middle=(Left+Right)//2
    return 'NotFound'+str(Count)




#print(list_of_numbers)
#print(search(list_of_numbers,minimum(list_of_numbers)))
print(search(list_of_numbers,56))
print(binary_search(list_of_numbers,56))