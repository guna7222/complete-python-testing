# A class is a blueprint to create an object
# __init__ is a constructor method that runs when an object is created.
# self refers to the current object
class SimpleInterestCalculator:
    def __init__(self, principal, time, rate):
        self.principal = principal
        self.time = time
        self.rate = rate # these values are stored as object variables using self

    def calculate_interest(self):
        interest = (self.principal * self.rate * self.time) / 100
        return interest


p = float(input("Enter Principal Amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter Time: "))

interest_cal_obj = SimpleInterestCalculator(p, r, t)
print(interest_cal_obj.calculate_interest())
