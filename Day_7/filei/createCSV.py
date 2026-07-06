# csv = "comma separated values", a simple text format for table-like data.
# The csv module helps us read/write that format correctly (e.g. handling commas).
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# "a" = append mode: adds new lines to the end of the file instead of
# overwriting it. newline="" is recommended by Python's docs when writing
# csv files on Windows, to avoid extra blank lines being inserted.
with open ("new_students.csv", "a", newline="") as file:
    # csv.writer writes plain rows (lists), e.g. writer.writerow([name, home]).
    # writer = csv.writer(file)
    # writer.writerow([name, home])

    # csv.DictWriter writes rows from a dictionary instead of a list.
    # Why: dictionaries let us write columns by name ("name", "home")
    # instead of remembering the column order, which is less error-prone.
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})