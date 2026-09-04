class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = name

    # @classmethod
    # def changeName(classss, name):
    #     classss.name = name

p1 = Person()
p1.changeName("Apil")
print(p1.name)
print(Person.name)