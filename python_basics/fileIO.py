#Njane Alvin
#24.02.2026
#Program to perform file operations

# create a new file
new_file = open("Students data.txt","r+")


#Write to new file
new_file.write("Student Name: James , ID :20906069 , Email : jamesiskrashingout@gmail.com ")
new_file.close()



#Read from file
new_file = open("Students data.txt","r+")
data = new_file.read()

print(data)
new_file.close()



#Delete file
#us on module
import os
os.remove("remove.txt")





# Delete folder