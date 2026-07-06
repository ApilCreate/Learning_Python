import csv

students =[]

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})

#or

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lamda means anonomous function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['house']}")

