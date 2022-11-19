class Account():
    def __init__(self, name):
        account_name = self.account_name = name
        account_balance = self.account_balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance = amount
                return True
            else:
                return False
    def get_balence(self):
        if amount == 0:
            return 0
        else:
            return amount
    def get_name(self):
        return name


