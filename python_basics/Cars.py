#Njane Alvin
#23.2.2026
# Program to show classes in python

class Car():
    # Attributes of the car 
    def __init__(self, model, make, color):
     self.model = model
     self.make = make
     self.color = color

#Print car details

    def print_details (self,model,make,color):
        print(f"{make} {model} of color {color} is a very good car")


#Instantiate a class object

my_favorite_car= Car("SRT","Dodge","Black") 
dads_car= Car("Land cruizer","Toyota", "Blue")

my_favorite_car.print_details("SRT","Dodge","Black")

