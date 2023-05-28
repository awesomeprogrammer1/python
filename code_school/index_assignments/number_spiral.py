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


n = int(input("Enter the size of the spiral: "))

# Create an empty n x n matrix
matrix = [[0] * n for i in range(n)]
print(matrix)
# Initialize variables
x, y = 0, 0
dx, dy = 0, 1
# dx, dy = 0,1 - right, dx,dy = 1, 0 -down dx,dy = 0, -1 - left dx, dy = -1, 0 -up
# Fill the matrix with numbers in spiral order
for i in range(n*n):
    matrix[x][y] = i + 1
    if x + dx < 0 or x + dx == n or y + dy < 0 or y + dy == n or matrix[x+dx][y+dy]:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy
print(matrix)
# Print the matrix
for row in matrix:
    for val in row:
        print('{:2d}'.format(val), end=' ')
    print()
