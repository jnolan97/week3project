class Rental():
    def __init__(self,income,expenses):
        self.income = income
        self.expenses = expenses
    
    #calculate cash flow
    def cashFlow(self):
        return print(self.income - self.expenses)
    #Method to calculate expenses based on user input
    def calcExpenses(self):
        self.expenses = int(input("What are your expenses? "))
        return self.expenses
    #Method to calculate income based on user input
    def calcIncome(self):
        self.income = int(input("What is the income you will be earning? "))
        return self.income
    #Method to calculate ROI
    def cashROI(self):
        try:
            down_payment = int(input("What did you put down on this house? "))
            costs = int(input("What were your closing costs? "))
            rehab = int(input("What did you spend on fixes? "))
            total_cost = down_payment + costs + rehab
            annual = (self.income * 12) - (self.expenses * 12)
            invest = (float(annual / total_cost) * 100)
            print(invest,"%")
        except Exception:
            print("Only integers allowed")

def run():
    buyer = Rental(2000,1610)
    while True:
        response = input("What do you want to do today? (Calculate cash flow / ROI / Exit) ")
        if response.lower() == "cashflow":
            buyer.calcIncome()
            buyer.calcExpenses()
            buyer.cashFlow()
        if response.lower() == "roi":
            buyer.calcExpenses()
            buyer.calcIncome()
            buyer.cashROI()
        if response.lower() == "exit":
            break
run()
