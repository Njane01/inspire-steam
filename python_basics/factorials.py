#Njane Alvin
#16.02.2026
#Program to calculate the factorials of numbers


number = int(input("Enter the number x : "))
factorial=1 #Initialise factorial on 1

for x in range(1,number+1):
    factorial*=x

    
print(f"{number}!={factorial}")


