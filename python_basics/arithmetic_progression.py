#Name : Njane Alvin
#Date : 13.02.2026
# program to calculate arithmetic progression

#calculating the nth term 

a=int(input("enter the first term :"))
n =int(input("Enter the number of terms :"))
d=int(input ("Enter the common difference"))

nth_term= a + (n-1) * d
print(f"The nth term is : {nth_term}") 


Sn=(n/2)* (2*a + (n-1)*d)
print(f"The sum of the numbers is: {Sn}")
