#Njane Alvin
#13.02.2026
# program for geometric progressions

#calculating the nth term

a=int(input("Enter the first term :"))
r=int(input("Enter the common ratio : "))
n=int(input("Entet the term number :"))

nth_term=(a) * (r**(n-1))
sn = (a * (r**n-1)) / (r-1)
print(f"The nth term is : {nth_term}")
print(f"The sum of n terms is: {sn}")

