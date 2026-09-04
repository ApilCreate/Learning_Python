# Exercise: Student class (practice encapsulation & abstraction)
#
# Build a Student class that stores a name and a score (0-100).
#
# Encapsulation:
# 1. Make score a private attribute (self.__score).
# 2. Write a method set_score(self, score) that only updates __score if the
#    value is between 0 and 100. If it's not, print "Invalid score" and
#    don't change anything.
# 3. Write a method get_score(self) that just returns __score.
# 4. From outside the class, try student.__score = 500 directly - notice it
#    does NOT actually change the real private value (this is the whole
#    point of encapsulation: you're forced to go through your methods).
#
# Abstraction:
# 5. Write a method get_grade(self) that returns a letter grade based on
#    the score:
#      90+     -> "A"
#      75-89   -> "B"
#      50-74   -> "C"
#      below 50 -> "F"
#    The person using your class just calls student.get_grade() - they
#    don't need to know or write the if/else logic themselves. That's
#    abstraction: hiding the messy details behind one simple method call.
#
# Try it:
# s = Student("Apil", 85)
# s.set_score(150)      # should print "Invalid score", score stays 85
# print(s.get_grade())  # should print "B"

class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def set_score(self, score):
        if score >= 0 and score <= 100:
            self.__score = score
        else:
            print("Invalid Score")
    
    def get_score(self):
        return self.__score
    
    def get_grade(self):
        if self.get_score() >= 90:
            return "A"
        if self.get_score() >= 75 and self.get_score() <= 89:
            return "B"
        if self.get_score() >= 50 and self.get_score() <=74:
            return "C"
        else:
            return "F"


st1 = Student("Apil", 500)
# st1.__score()

print(st1.get_score())


s = Student("Apil", 85)
s.set_score(150)      # should print "Invalid score", score stays 85
print(s.get_grade())  # should print "B"