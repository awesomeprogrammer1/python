'''
Given a number n, create a str with numbers that go from 1 to n^2
If you aren't able to print it in a spiral-ordered format (see output example 1)
You may do it in a list format (see output example 2)

Example:

Input: 5 (n=5)

Output (example 1):
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

Output (example 2):
[1, 2, 3, 4, 5, 16, 17, 18, 19, 6, 15, 24, 25, 20, 7, 14, 23, 22, 21, 8, 13, 12, 11, 10, 9]
'''

def number_spiral(n: int) -> str:
    num_spiral_list = []
    for i in range(n^2+1):
        num_spiral_list.append[i]
    
