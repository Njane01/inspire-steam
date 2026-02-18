#Name : Njane Alvin
#Date : 18.02.2026
# program to show lists in python


friends=[ "James", "Alvin","Elvis","Augustine"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Mwass")
print(friends)

new_friends=["Dan","Dabney","Faith","Wendi","Bob"]
print(len (new_friends))
#New list of students
students= friends+new_friends
print(students)
students.pop()
print(students)
students.insert(4,"Joe")
print(students)

students.insert(9,"Joeeellll")
print(students)
students.extend("Mahia")
print(students)

students.remove("Dabney")
print(students)

new_friends=students.copy()
print(new_friends)