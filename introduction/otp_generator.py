import random

otp = random.randint(100000, 999999)
print(otp)

otp_entered_by_user = int(input("Enter Otp"))

if otp_entered_by_user == otp:
    print("Success")
else:
    print("Invalid Otp")
