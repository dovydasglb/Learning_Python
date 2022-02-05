# Lists are created using square brackets (ordered, allow duplicates, changeable (change/add/remove), allow
# multiple data types):
my_list = ['a', 3, 'a', True, 2.0]
print(my_list)
print(type(my_list))
# can also be created using:
my_list = list(('a', 3, 'a', True, 2.0))
print(my_list)
print(type(my_list))

# Lists are zero indexed:
print(my_list[0])
print(my_list[-1])
print(my_list[2:4])
print(my_list[-3:-1])
print(my_list[:3])
print(my_list[2:])

# To check if an item in the list exists:
if 'a' in my_list:
    print(True)
else:
    print(False)

# To change items in a list:
my_list = [1, 2, 3, 4, 5, 6]
my_list[2] = 'changed item'
print(my_list)
my_list = [1, 2, 3, 4, 5, 6]
my_list[1:2] = ['a', 'b', 'c']
print(my_list)

# To change a range of items in a list:
my_list = [1, 2, 3, 4, 5, 6]
my_list[2:4] = ['a', 'b', 'c']
print(my_list)
my_list = [1, 2, 3, 4, 5, 6]
my_list[2:] = []
print(my_list)
my_list = [1, 2, 3, 4, 5, 6]
my_list[1:3] = ['a', 'b', 'c', 'd']
print(my_list)

# To insert an item into a list or append:
my_list = [1, 2, 3, 4, 5, 6]
my_list.insert(3,'a')
my_list.append('b')
print(my_list)

# To append another list (or other iterable item) onto the list:
my_list = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
my_tuple = (True, False)
my_list.extend(my_list2)
my_list.extend(my_tuple)
print(my_list)
print(type(my_list))

# To remove a specific item from a list:
my_list = [1, 2, 3, 'String', 4, 5, 6, 'String']
my_list.remove('String')
print(my_list)
# Note this will only remove the first instance of the specified item

# To remove an item at a specific index:
my_list = [1, 2, 3, 4, 5, 6]
my_list.pop(2)
print(my_list)
# Or:
my_list = [1, 2, 3, 4, 5, 6]
del my_list[0]
print(my_list)

# To remove the last item from a list:
my_list = [1, 2, 3, 4, 5, 6]
my_list.pop()
print(my_list)

# We can also remove all items from the list to make it empty:
my_list = [1, 2, 3, 4, 5, 6]
my_list.clear()
print(my_list)

# To create a copy of a list use:
my_list = [1, 2, 3, 4, 5, 6]
my_list2 = my_list.copy()
print(my_list2)
# Or alternatively use:
my_list3 = list(my_list)
print(my_list3)
# This is in contrast to assigning a list to a new variable as this would just reference original list:
my_list = [1, 2, 3, 4, 5, 6]
my_list2 = my_list
my_list.clear()
print(my_list2)