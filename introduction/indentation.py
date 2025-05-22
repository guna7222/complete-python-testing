"""
What is Indentation?

Indentation refers white spaces at the beginning of the code, where in other programming languages
indentation is used for code readability but in python indentation refers a ' block of a code '
"""

vote_eligibility = 18

def validate_age(age):
    if age >= vote_eligibility:
        print("Eligible to Vote current age: {}".format(age))
    else:
        years_to_get_vote_eligibility = vote_eligibility - age
        print("Not Eligible to Vote Current Age is: {} you have to wait {} years to get Eligible".format(age, years_to_get_vote_eligibility))

client_age = int(input("Enter Age:- "))
validate_age(client_age)