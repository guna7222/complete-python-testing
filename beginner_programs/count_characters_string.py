# Count characters in a string

class CountCharactersInString:
    count_characters = 0  # class level variable it can be used for all the instances

    def __init__(self, computer_name):
        self.computer_name = computer_name

    def count_characters_in_string(self):
        name = self.computer_name
        for x in name:
            CountCharactersInString.count_characters += 1
        return CountCharactersInString.count_characters


    def print_message(self):
        count = self.count_characters_in_string()
        print(f"Characters In a String {count}")


user_input_for_string = str(input("enter a string:- "))

count_object = CountCharactersInString(user_input_for_string)
count_object.print_message()