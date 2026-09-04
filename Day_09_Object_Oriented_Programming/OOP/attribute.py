# attributes

class Student:
    college_name = "ABC COllege"
    # name = "anonymous"  #class attr
    # Default constructors
    def __init__(self):

        print("Default")


    # Parameterized constructors
    def __init__(self, fullname, marks):
        self.name = fullname #obj attr > class attr
        self.marks = marks
        print("Adding new student in DB...")

    def welcome(self):
        print("Welcome student")

    def get_marks(self):
        return f"Hi {self.name}, your total marks is {self.marks}"

s1 = Student("Apil", 50)
print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())

s2 = Student("Soni", 60)
print(s2.name, s2.marks)

print(Student.college_name)




