class Expense():
    def __init__(self,name,category,amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        print(f"Expense: {self.name}, Category: {self.category}, Amount: {self.amount}")