# data types

"""
str,
int, float, complex
list, tuple, range
set, frozenset
dict,
bool
bytes, bytearray, memoryview
None
"""

#str
name = "Text"

#int
a = 10
#float
b = 12.5
#complex
c = 1j

# list
list_example = [1,2,3,4, "Hello"]

# tuple
tuple_range = (1,2,3,'python')

#range
range_example = range(2)
print(range_example)

# set
set_ex = {1,2,3}
print(type(set_ex))

# dict
dict_example = {"name":"Guna", 2:"value", 2.5:"float"}
print(dict_example)

# bool
isTrue = True

bytes_ex = b"Hello"
print(bytes_ex)

# Setting specific data type

pro_name = str('python')

age = int(27)

interest = float(2.5)

list1 = list(("name", 1, 2, 4))

tuple1 = tuple(('tuple', 2.5, 9, True))

print(range(5))

set1 = set(("name", 2, 6.4, True))

dict1 = dict(name="python3", age=25)

print(bool(False))

print(None)