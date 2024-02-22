class Category:
  def __init__(self,name):
    self.ledger = []
    self.name = name
    
  def deposit(self, amount, description=""):
    deposit_list = {'amount': amount, 'description':           description}
    self.ledger.append(deposit_list)

  def check_funds(self,amount):
    balance = 0
    for adding in self.ledger:
      balance += adding['amount']
    if float(balance) >= amount:
      return True
    else:
      return False
  
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      withdraw_list = {'amount': float(amount)*-1, 'description': description}
      self.ledger.append(withdraw_list)
      return True
    else:
      return False

  def balance(self):
    current_balance = 0
    for current in self.ledger:
      current_balance += current['amount']
    return current_balance

  def transfer(self, amount, other_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {other_category.name}")
      other_category.deposit(amount, f"Transfer from {other_category.name}")
      return True
    else:
      return False

  def __repr__(self):
    title_line = self.name(30,"*") + "\n"
    for item in self.ledger:
      display = f"{item['description']} + {item['amount']:7.2f} + \n"
      total = f"Total: {self.balance()}"
    return title_line + display + total

def create_spend_chart(categories):
  chart = "Percentage spent by category"
  total = 0
  total_spent = []
  spent_percents = []
  for category in categories:
    spent = 0
    for money in category.ledger:
      if money['amount'] < 0:
        spent += (money['amount']*-1)
        total_spent.append(spent)
        total += spent
  for money_spent in total_spent:
    spent_percents.append((money_spent/total)*100)
  
    
        


    
      
    
    
    
  


