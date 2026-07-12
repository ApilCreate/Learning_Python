class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")


car1 = Car()
car1.start()

#Abstarction ->
# Hiding the implementation details of a class and only showing the essential features to the user

#Encapsulation ->
# Wrapping data and functions into a single unit(object).