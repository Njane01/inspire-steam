#Njane Alvin
# 23.02.2026
#Program to show inheritence in python
class Animal():


    def __init__(self,species,weight,food):
     self.species= species
     self.weight = weight
     self.food = food

     def grow (self,weight):
        weight = 1.1*weight
        print("The animal weightis {weight} in Kilograms")
    def eat (self,food):
       print("the animal eats {food}")

class Dog(Animal):


    def __init__(self,species,weight,breed):
     
     
     
        super().__init__(species,weight,food):  
        self.species= species
        self.weight= weight
        self.breed = breed

    def barks (self,barks):
        
        
        print("The dog says woof woof")

    def eat (self,food):
       print("the Dog eats {food}")
       




class Horse (Animal):



    def __init__(self,species, weight,food):
     self.species= species
     self.weight = weight
     self.food = food

     def neigh(self):
        print("The horse says neeeiiiigggghhhhh")   
    def eat (self,food):
       print("the animal eats {food}")
       
