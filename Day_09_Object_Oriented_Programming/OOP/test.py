#Create student class that takes name & marks of 3 students as arguments in constructor. Then create a method to print the average

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = 0
        for val in self.marks:
            total += val
        return (total/3)
    

a = Student("Apil", [50, 70, 90])

print(f"Student names{a.name}, got the average marks of {a.average()}")