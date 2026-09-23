class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Expense: {self.name}, Category: {self.category}, Amount: {self.amount}"

    def __repr__(self):
        return self.__str__()