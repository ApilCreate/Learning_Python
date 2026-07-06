import csv

students =[]

# csv.reader automatically splits each line by comma for us, so we don't
# have to call .rstrip().split(",") ourselves like in the manual version below.
# Each row comes back as a list, e.g. ["Hermione", "Gryffindor"], and since
# we know there are always exactly 2 columns, we can unpack it into
# name, house directly in the for-loop.
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})

#or (doing the same thing manually, without the csv module)

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lambda means an anonymous (unnamed) function, written inline.
# Here it tells sorted() "use each student's name as the sort key".
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['house']}")

