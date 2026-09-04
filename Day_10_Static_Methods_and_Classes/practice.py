#Create Account class with 2 attributes - balance & account no.
#Create method for debit, credit & printing the balance

#1->

class Account:

    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance: ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance: ", self.balance)


    def get_balance(self):
        return self.balance


user1 = Account(10000, 12345)

print(user1.balance)
print(user1.acc)

user1.debit(1000)
user1.credit(2500)
