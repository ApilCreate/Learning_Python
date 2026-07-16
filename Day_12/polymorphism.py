#Poly means many and morp means forms
#Operator overloading
# print(1 + 2) #3
# print("Apil" + " " + "Neupane") #concatenate
# print([1,2,3] + [4,5,6]) #merge

#complex numbers

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNum(self):
        print(self.real,"i +", self.imag,"j")

    def __add__(self, set2):
        newReal = self.real +set2.real
        newImag = self.imag +set2.real
        return Complex(newReal, newImag)
    
    def __sub__(self, set2):
        newReal = self.real - set2.real
        newImag = self.imag - set2.real
        return Complex(newReal, newImag)

num1 = Complex(4,6)
num1.showNum()

num2 = Complex(4,4)
num2.showNum()

num3 = num1 + num2
num3.showNum()

num4 = num1 - num2
num4.showNum()