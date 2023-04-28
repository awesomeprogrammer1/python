"""
Output a table of size
n*n, filled with numbers from 1 to n^2 in a spiral
coming out of the upper left corner and twisting clockwise, 
as shown in the example (here n=5):

1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

[1, 2, 3, 4, 5, 16, 17, 18, 19, 6, 15, 24, 25, 20, 7, 14, 23, 22, 21, 8, 13, 12, 11, 10, 9]
"""


def number_sprial(n: int) -> list:
    num_spiral: list = []
    for i in range(1, n ^ 2 + 1):
        num_spiral.append[i]
    
 