# Collections (arrays) are 'containers' used to store multiple data entries inside a variable
# Commonly used Python built-in collections are: Lists, Tuples, Sets and Dictionaries

# Lists are created using square brackets (ordered, allow duplicates, changeable (change/add/remove), allow
# multiple data types):
my_list = ['a', 3, 'a', True, 2.0]
print(my_list)
print(type(my_list))
# can also be created using:
my_list = list(('a', 3, 'a', True, 2.0))
print(my_list)
print(type(my_list))

# Tuples are created using round brackets (ordered, allow duplicates, unchangeable, allow multiple data types):
my_tuple = ('a', 'a', 3, True, 2.0)
print(my_tuple)
print(type(my_tuple))
# can also be created using:
my_tuple = tuple(('a', 'a', 3, True, 2.0))
print(my_tuple)
print(type(my_tuple))

# Sets are created using curly brackets (unordered, no duplicates (will only store a single instance of
# repeated item), unchangeable (except add/delete items) and allow multiple data types:
my_set = {'a', 'a', 3, True, 2.0}
print(my_set)
print(type(my_set))
# can also be created using:
# noinspection PySetFunctionToLiteral
my_set = set(('a', 'a', 3, True, 2.0))
print(my_set)
print(type(my_set))

# Dictionaries are created using curly brackets and contain key:value pairs (ordered, no duplicates (cannot
# have values with the same key), changeable (change/add/remove), can contain multiple data types (both keys and
# values)):
my_dictionary = {
    1: 2020,
    2: 'September',
    'brand': 'Apple',
    'product': 'iPhone',
    'current model': False
}
print(my_dictionary)
print(type(my_dictionary))
# can also be created using (note parentheses):
my_dictionary = dict({1: 2020, 2: 'September', 'brand': 'Apple', 'product': 'iPhone', 'current model': False})
print(my_dictionary)
print(type(my_dictionary))
