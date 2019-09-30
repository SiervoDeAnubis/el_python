# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Cesarin'
age = 34

# Concatenate

print('Hello World ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position

print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name

print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+)

print(f'My name is {name} and I am {age}')

# String Methods

# Capitalize first letter

s = 'hello world!'

print(s.capitalize())

# s.upper()
# s.lower()
# s.swapcase()
# s.replace()
# s.startswitth('string')
# s.endswith('string')
# s.split() Split into a list which is like an array
# s.find('string') Find position of any character
# s.isalnum() is alphanumeric
# s.isalpha() is for alphabetic
# s.isnumeric() is all numbers

print(s.replace('world!', name))

# Get Length

print(len(s))

# Count
sub = 'h'

print(s.count(sub))
