import math
a = int(input("Enter number of rows : "))


def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end = " ")

        for j in range(i+1):
            print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)),end = ' ')
        print()

pascal_triangle(a)