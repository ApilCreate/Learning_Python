# #Dictionary

# #Basically it means objects
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }


# print(students["Hermione"])
# print(students["Draco"])
# print(students["Harry"])
# print(students["Ron"])

# for student in students:
#     print(student, students[student], sep=": ")

students = [
    {"name": "Hermione",
     "house": "Gryffindor",
     "patronus": "Otter"},

     {"name": "Harry",
     "house": "Gryffindor",
     "patronus": "Stag"},

     {"name": "Ron",
     "house": "Gryffindor",
     "patronus": "Jack Russel terrier"},
     
     {"name": "Draco",
     "house": "Slytherin",
     "patronus": None},
]

for i in range(len(students)):
    print(i+1, students[i])