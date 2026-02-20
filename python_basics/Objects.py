#Njane Alvin
#19.02.2026
# Njane Alvin
# 19.02.2026

class Human:
    # Define the attributes of humans
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True

    # Constructor
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    # Method
    def tell_story(self):
        print(f"Hello. I am {self.human_name}. I have a story to tell.")
        print("There once lived a guy who had a car.")


# Creating the human
Elvis = Human("Elvis", 17)

# Let the human do things
Elvis.tell_story()

print("Elvis's age is:", Elvis.human_age)


#Modify the object

Elvis.city = "Kiambu"


print("Elvis' location is" ,Elvis.city)
