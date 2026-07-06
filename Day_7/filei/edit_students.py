import csv

students =[]

# csv.DictReader reads each row straight into a dictionary, using the
# first line of the csv file as the column names (keys) automatically.
# Why: this is even simpler than csv.reader, since each row already
# comes back as {"name": ..., "house": ...} instead of a plain list.
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({"name": row["name"], "house": row["house"]})
        students.append(row)

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

