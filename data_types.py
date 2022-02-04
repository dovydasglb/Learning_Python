# Python is a dynamically typed language so the data types of variables are assigned automatically
# Data types describe what kind of data is stored within a variable and what rules apply to manipulating that data

# There are 4 main types of variables that are most common:
a = 5           # is an integer
print(a)
b = 'string'    # is a string
print(b)
c = 5.1234      # is a float (floating point number)
print(c)
d = True        # is a boolean
print(d)

# You can the find data type using:
print(type(d))

# You can set the specific the data type using:
x = 5
y = str(x)
print(type(x))
print(type(y))

# You can also specify the data type when creating a variable:
x = float(5)
print(x)
print(type(x))

# Aside from the main data types there are other data types which can be grouped under categories:
"""
Text Type:          str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:       dict
Set Types:          set, frozenset
Boolean Type:       bool
Binary Types:       bytes, bytearray, memoryview
"""