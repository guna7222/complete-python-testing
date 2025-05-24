# prime number

class PrimeNumber:

    def __init__(self, number):
        self.number = number

    def prime_number(self):
        if self.number <= 1:
            print(f"Not a prime number {self.number}")
        else:
            for i in range(2, self.number):
                if  self.number % i == 0:
                    print(f"not a prime number {self.number}")
                    break

            print(f" prime number: {self.number}")

user_prime_number = int(input("enter a number: "))
prime_number_obj = PrimeNumber(user_prime_number)
prime_number_obj.prime_number()