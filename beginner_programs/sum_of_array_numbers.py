class SumOfArrayNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_array_numbers(self):
        sum_array_numbers = 0
        for x in self.numbers:
            sum_array_numbers += x

        return sum_array_numbers


array_values = [10, 20, 50, 100]
sum_of_array_numbers_object = SumOfArrayNumbers(array_values)

result = sum_of_array_numbers_object.sum_array_numbers()
print(result)