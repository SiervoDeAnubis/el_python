# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1 # int
# y = 2.5 # float
# name = 'Brand' # string
# is_cool = True # bool

# Multiple assigment
x, y, name, is_cool = (1, 2.5, 'Cesarin', True)

# imprint
# just remember in python2 we don't use parethesis
print(x)

print(x, y, name, is_cool)

# Basic Maths

a = x + y
print(a)

# Casting
x = str(x)

# Check Type
print(type(x))
