class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Tech", "70000")

e1 = Employee("Intern", "Backend Engineer", "50000")
print(e1.showDetails())

e2 = Engineer("Apil", 21)
e2.showDetails()