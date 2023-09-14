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
  def total_withdrawals():
    for item in self.ledger:
      if item['amount'] < 0:
        total_withdrawals += item['amount']
    return total_withdrawals
#end class Category

def create_spend_chart(categories):
  chart = list()
  bubbles = list()
  bubbles.append("   ") # bubbles[0] false
  bubbles.append(" o ") # bubbles[1] true
  # stays outside of class
  # takes the list of categories and returns a string that is a bar chart
  # Bar Chart
  # title at the top that says "Percentage spent by category".
  # Shows percent of
  # This function will be tested with up to four categories.
  #chart[0] = "Percentage spent by category")
  chart.append("Percentage spent by category\n")
  #chart[1] = "100|"
  #chart[2] = " 90|"  # etc

  # spaces between categories are always 2
  # " " + character + " ", then extra space before "\n"
  # 14 wide for 3 categories:
  # 3 for left side
  # 1 for "|"
  # 9 (3*3) for bubbles " o "
  # 1 " " before the "\n"
  # Letters will need to be lined up with bubbles, so
  # 4 empty spaces before the first, then
  # " " + char + " ", each item, then trailing " \n"
  # 4,3*x,
  # Is this a percentage of all expenditures or a percentage of available income?
  #
  # Final space of last line is not part of \n, it is still there on last line
  # only as many vertical lines as chart + length of longest word