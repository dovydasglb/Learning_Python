# There are 4 main types of variables that are most common:
a = 5           # is an integer
print(a)
b = 'string'    # is a string
print(b)
c = 5.1234      # is a float (floating point number)
print(c)
d = True        # is a boolean
print(d)

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

