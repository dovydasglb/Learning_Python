# There are 4 main types of variables that are most common:
a = 5           # is an integer
print(a)
b = 'string'    # is a string
print(b)
c = 5.1234      # is a float (floating point number)
print(c)
d = True        # is a boolean
print(d)

# Each variable is a reference to a section in memory that is reserved for storing data:
print(id(d))
print(hex(id(d)))

# Declaring string variables:
x = 'a string'
print(x)
# is the same as:
x = "a string"
print(x)
# also, the same as:
x = '''a long string that can span multiple lines
 (this is the same string but on another line)'''
print(x)
# or:
x = """a long string that can span multiple lines
 (this is the same string but on another line)"""
print(x)

# Also, double quotation marks can be used to avoid using escape keys:
x = "couldn't use a single quotation mark ' without escape key if used them to declare a string"
print(x)
x = 'this works both ways, i.e. you can use "double quotation marks" within single ones'
print(x)

# Variables are case sensitive:
a = 7
print(a)
# will not overwrite
A = 'variable A'
print(A)

# You can create multiple variables in one line:
x, y, z = 'This is x', 5, True
print(x)
print(y)
print(z)

# Likewise, you can assign a value to multiple variables in one line:
x = y = z = True
print(x)
print(y)
print(z)

# You can also 'unpack' a collection into variables:
some_collection = ['a', 'b', 'c']
x, y, z = some_collection
print(x)
print(y)
print(z)

# String variables can be combined using operator plus operator:
x = 'this'
y = ' was combined together'
z = x + y
print(z)
# However, math operators used on numerical variables will instead carry out the math:
x = 5
y = 3
print(x+y)

# All the variables created outside a function are global:
x = 'x is global'
# and global variables can be called upon within the function:


def my_function():
    return x


print(my_function())
# However, variables declared within functions are local to that function. To make them global use:


def my_function():
    global x
    x = 5


my_function()
print(x)
# Order for variables is as follows: built-in>global>local
