# Name : Njane Alvin
# Date: 17/02/2026
# Program to draw a diamond  and triangle using asterisks

n = 5 # number of rows
# upper half of the diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
# lower half of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


# Program to draw a triangle shape using asterisks
n = 5 # number of rows
print("__________________________________________________________________")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
