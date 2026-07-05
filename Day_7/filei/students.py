with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

students =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lamda means anonomous function
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} lives in {student['house']}")

