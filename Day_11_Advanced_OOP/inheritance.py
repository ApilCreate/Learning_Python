# Inheritance

# Single and multi-level interitance
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")


# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand


# class BMW(ToyotaCar):
#     def __init__(self, type):
#         self.type = type
        

# car1 = BMW("Petrol")
# car1.start()

# Multiple Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)


# super method

class Car:

    def __init__(self, type):
        self.type = type

    
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)