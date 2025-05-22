"""
Variables are containers for storing data values

the variables are created the moment when you assign a value to it.

Python is a dynamic programming language, where you don't have to specify the data type before declaring variable
"""

age = 18
name = "Test1"

# Casting
x = str(5) # type string '5'

y = int(x) # type of int 5
print(type(y))

f = float(3) # 3.0
print(f)

# type() function is used to know the type of the variable

# we can use single ' or double "" quotes for strings

# variable names are case-sensitive

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

# Many values to multiple variables
java, python, r = "Java-8,", "python-3,", "r"
print(java, python, r)

# One value to multiple variables

a = b = c = "single value"

# Unpack a collection

list_ex = [1,2,3,4]
one, two, three, four = list_ex
print(one, two, three, four)

#output variables print()

# Global Variables
# The variables declared outside a function is called global variables can be used both inside and outside a function.

feedback = "Great!"
def feed():
    print("python is {}".format(feedback))

feed()

# with the help of global keyword can we make local variable as global variable