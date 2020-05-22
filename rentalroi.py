class Rental():
    def __init__(self,income,expenses):
        self.income = income
        self.expenses = expenses
    
    #calculate cash flow
    def cashFlow(self):
        return print(self.income - self.expenses)
    #Method to calculate ROI
    def cashROI(self):
        down_payment = input("What did you put down on this house? ")
        costs = input("What were your closing costs? ")
        rehab = input("What did you spend on fixes? ")
        total_cost = float(down_payment + costs + rehab)
        annual = float((self.income - self.expenses) * 12)
        invest = float((annual / total_cost) * 100)
        print(invest,"%")

def run():
    buyer = Rental(2000,1610)
    while True:
        response = input("What do you want to do today? ")
        if response.lower() == "cashflow":
            buyer.cashFlow()
        if response.lower() == "roi":
            buyer.cashROI()
        if response.lower() == "exit":
            break
run()
