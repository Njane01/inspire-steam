# Njane Alvin
#17.02.2026
#Quadratic formulae
# Program to calculate the quadratic formula
import math
a = 1
b = -3
c = 2
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The roots are real and equal: {root}")
