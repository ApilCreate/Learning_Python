import csv

students =[]

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({"name": row["name"], "house": row["house"]})
        students.append(row)

#or

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lamda means anonomous function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['house']}")

