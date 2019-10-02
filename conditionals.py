# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 6

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple IF

if x == y:
    print(f'{x} is equal to {y}')

# IF/ELSE

if x > y:
    print(f'{x} is greater that {y}')
else:
    print(f'{x} is less than {y}')

# elif

if x > y:
    print(f'{x} is greater that {y}')
elif x == y:
    print(f'{x} is equal that {y}')
else:
    print(f'{x} is less than {y}')

# nested if

if x > 2:
    if x <= 10:
        print(f'{x} is less than 2 and greater than 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# and operator

if x > 2 and x <= 10:
    print(f'{x} is less than 2 and greater than 10')

#  not opetator

if not(x == y):
    print(f'{x} is not equal {y}')

# in operator

numbers = [1, 2, 3, 4, 5, 6, 9, 10, 11]  # this is a list

if x in numbers:
    print(f'{x} exists in numbers list')
    print(x in numbers)

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# using not operator with in

if x not in numbers:
    print(x in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(x is y)

# is
if x is not y:
    print(x is not y)
