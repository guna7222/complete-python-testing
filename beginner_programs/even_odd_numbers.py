class EvenOrOddNumbers:
    def __init__(self, number):
        self.number = number

    def even_or_odd(self):
        if self.number % 2 == 0:
            return "Even Number {}".format(self.number)
        else:
            return "Odd Number {}".format(self.number)


# object creation
user_input = int(input("Enter Number: "))
even_or_odd_object = EvenOrOddNumbers(user_input)
print(even_or_odd_object.even_or_odd())