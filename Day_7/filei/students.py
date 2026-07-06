# This block reads the csv file manually, without the csv module,
# by treating it as plain text.
with open("students.csv") as file:
    for line in file:
        # rstrip() removes the trailing newline "\n" at the end of the line.
        # split(",") breaks the line into a list at each comma,
        # e.g. "Hermione,Gryffindor" -> ["Hermione", "Gryffindor"]
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

students =[]

with open("students.csv") as file:
    for line in file:
        # Unpacking: since split(",") always gives us 2 items here,
        # we can assign them directly to two variable names at once.
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# lambda means an anonymous (unnamed) function, written inline.
# Here it tells sorted() "use each student's name as the sort key".
# reverse=True sorts from Z to A instead of the default A to Z.
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} lives in {student['house']}")

