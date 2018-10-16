class CreditCard:
    def __init__(self, yearly_rate_in_percent):
        self.balance = 0
        self.yearly_rate_in_percent = yearly_rate_in_percent
    
    def get_balance(self):
        return self.balance
    
    def spend(self, amount):
        self.balance += amount
    
    def pay_bill(self, amount):
        self.balance -= amount
    
    def monthly_update(self):
        interest = self.get_balance()*self.yearly_rate_in_percent/12/100
        self.balance += interest
    
    def __str__(self):
        return "amount due: "+str(self.get_balance())