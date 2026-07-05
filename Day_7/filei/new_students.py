import csv

students =[]

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})



with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lamda means anonomous function
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} lives in {student['house']}")

