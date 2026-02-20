#Njane Alvin
#18.02.2026

...
def cook_egg():
    oil="20ml"
    Pan =True
    Moto = True
    eggs = 2
    print(f"The pan is {Pan} and the fire is {Moto}, add {oil} amount of oil and add {eggs} to the pan")

print("Here is statement 1")
print("Here is statement 2")

cook_egg() 


print("here is statement 3")
# Bus fare creating funtion


def create_fare(route,distance, is_rush_hour):
    fare = distance *10
    if is_rush_hour == True:
        fare = fare* 1.5
        
    print (f"Your fare to {route} is {fare}")

is_rush_hour =True
    
returned_fare =create_fare("Juja-Alsops", 7,True)

print(f"The retuned fare is {returned_fare}")

#Passing a list as a parameter

def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")

all_interests = ["Basketball","hiking","Painting","Poetry"]

write_all_interests(all_interests)



