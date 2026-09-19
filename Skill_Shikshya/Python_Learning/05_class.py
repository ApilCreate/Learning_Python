from abc import ABC, abstractmethod
#Class
class Student:
    class_year = 2026
    num_students = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Hari", 30)
student2 = Student("Shyam", 29)

print(Student.num_students)
print(student1.name)

#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# animal = Animal("Lion")
# print(animal.name)

# animal.eat()
# animal.sleep()

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

dog1 = Dog("Tucker")
print(dog1.name)
dog1.eat()
dog1.bark()
dog1.sleep()

#Multi heritance

class Animal:
    def __init__(self, name:str):
        self.name = name

    def Prey(self):
        print(f"{self.name} is fleeying.")

    def Predator(self):
        print(f"{self.name} is hunting.")

    class Rabbit(Prey):
        pass

    class Tiger(Predator):
        pass


