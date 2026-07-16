#del keyword

# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("APIL")
# print(s1.name)
# del s1
# print(s1.name)

#Private attributes

# class Account:
#     def __init__(self, acc_no, acc_pw):
#         self.acc_no = acc_no
#         self.__acc_pw = acc_pw


#     def reset(self):
#         print(self.__acc_pw)

# acc1 = Account(22222, "Password123")

# print(acc1.acc_no)
# print(acc1.__acc_pw)


# class Person:
#     __name = "anonymous"

#     @staticmethod
#     def __hello():
#         print("hello")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())