class Student:

    # Default constructors
    def __init__(self):

        print("Default")


    # Parameterized constructors
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student in DB...")

s1 = Student("Apil", 50)
print(s1.name, s1.marks)

s2 = Student("Soni", 60)
print(s2.name, s2.marks)

# class Car:
#     color = "blue"
#     brand = "BMW"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# car2 = Car()

