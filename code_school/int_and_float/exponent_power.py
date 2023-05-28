'''
Given a natural number N, find the largest integer power of two not exceeding N. 
Print the exponent and the power itself.

The exponentiation operation cannot be used!


'''

def exponent_power(n: int):
    counter = 0
    num = 1
    while n > num*2:
        counter += 1
        num *= 2
    else:
        return num, counter
    

print(exponent_power(35))