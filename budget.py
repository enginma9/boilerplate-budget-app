class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __str__(self):
    return self.show_reciept()

  def __repr__(self):
    return self.show_reciept()

  def show_reciept(self):
    total = 0
    reciept = f"{self.name:*^30}" + "\n"
    # Last line: "Total:" + 7 char
    for item in self.ledger:
      str_amount = str("{:.2f}".format(item["amount"]))
      reciept += f"{item['description'][0:23]:<23}" + f"{str_amount:>7}" + "\n"
      total +=item['amount']
    reciept += "Total: " + str(total)
    return  reciept

  def deposit(self, amount, description=""):
    # append ledger list with
    # { "amount": amount,"description": description }
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, negate, description=""):
    # append ledger list with
    # { "amount": amount,"description": description }
    # if able to withdraw, return true, else, return false
    # use check_funds()
    if (self.check_funds(negate)):
      self.ledger.append({"amount": -negate, "description": description})
      return True

    else:
      return False

  def get_balance(self):
    balance = 0
    for dict in self.ledger:
      balance += dict["amount"]
    return balance

  def transfer(self, amount, category):
    # use check_funds()
    if (self.check_funds(amount)):
      # The method should add a withdrawal with the amount and the description
      # "Transfer to [Destination Budget Category]".
      self.withdraw(amount, "Transfer to " + category.name)
      # The method should then add a deposit to the other budget category
      # "Transfer from [Source Budget Category]"
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    # just checks:
    # if amount left in budget >= amount, return true, else false
    if (self.get_balance() >= amount):
      return True
    return False
  # end check_funds  
  def total_withdrawals(self):
    withdrawals = 0
    for item in self.ledger:
      if item['amount'] < 0:
        withdrawals += item['amount']
    return withdrawals
# end class Category

def create_spend_chart(categories):
  chart = list()
  bubbles = list()
  bubbles.append("   ") # bubbles[0] false
  bubbles.append(" o ") # bubbles[1] true
  #Set up chart base
  chart.append("Percentage spent by category") #0
  chart.append("100|")#1
  chart.append(" 90|")#2
  chart.append(" 80|")#3
  chart.append(" 70|")#4
  chart.append(" 60|")#5
  chart.append(" 50|")#6
  chart.append(" 40|")#7
  chart.append(" 30|")#8
  chart.append(" 20|")#9
  chart.append(" 10|")#10
  chart.append("  0|")#11
  chart.append("    ") #12 line for dashes
  # Get longest name, and put in dashes
  longest=0
  names = list()
  combined_withdrawals = 0
  for category in categories:
    names.append(category.name)
    if len(category.name) > longest:
      longest = len(category.name)
    # end if
    chart[12] += "---"
    
    combined_withdrawals += category.total_withdrawals()
  # end for
  # iterate through to create space for letters of the names 
  #print(combined_withdrawals)
  #print( longest)
  for i in range(longest):
    chart.append("    ") #13..longest title.length()
    #print(longest)
    # Build bottom
    for name in names:
      if i >= len(name):
        chart[i+13] += "   "
      else:
        chart[i+13] += " " + name[i] + " "
      # end for name
  # end for i
  percentages = list()
  for i in range(len(categories)):
    percentages.append( int( 10 * categories[i].total_withdrawals() / combined_withdrawals ))
    for x in range(11):
      if 10 - x > percentages[i]:
        # add bubble[0/1] to this line
        chart[x+1] += bubbles[0]
      else:
        chart[x+1] += bubbles[1]
  for i in range(len(chart)):
    if i == 12:
      chart[i] += "-"
    elif i == 0:
      continue          
    else:
      chart[i] += " "
    print(chart[i])
    # Return with newlines in string
  print("\n".join(chart))
  return "\n".join(chart)