# A List is a collection which is ordered and changeable. Allows duplicate members.
# it is basically an array

# Create List
# numbers = [1, 2, 3, 4, 5] <---- this the most popular way to create a list in python

# Using a constructor
# <---- we can use the construct list to create a list
numbers = list((1, 2, 3, 4, 5))
fruits = ['Apples', 'Orange', 'Grapes', 'Pears']

# print(type(numbers))

# Get Value
print(fruits[1])

# Get Len
print(len(fruits))

# Append to list
fruits.append('Mangos')

print(fruits)

# Remove from list

fruits.remove('Grapes')

print(fruits)

# Insert into position

fruits.insert(2, 'Strawberries')

print(fruits)

# Remove from position

fruits.pop(3)

print(fruits)

# Reverse list

fruits.reverse()

print(fruits)

# Sort list

fruits.sort()

print(fruits)

# Reverse Sort

fruits.sort(reverse=True)

print(fruits)
