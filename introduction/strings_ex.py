# strings in python are array of bytes representing unicode characters

name = "guna"

multiline_strings = """
example
"""

loop_through_string = "python"

for x in loop_through_string:
    print(x)


# slicing example

slicing = "java"
print(slicing[0:])

print(len(slicing))

# concatenation

# f strings are formated strings

checking = "hell world"
if "world" in checking:
    print("True")


if "world" not in checking:
    print("not there")


"""
upper()
lower()
replace()
strip()
split(",")
center(10, "0")
capitalize()
casefold()
count(value, start, end) start and end are optinal 
endswith(value, start, end)
"""