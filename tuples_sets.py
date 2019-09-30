# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple doesn't support idle assignment
# Simple Tuple

fruit_tuple = ('Apple', 'Orange', 'Mango')

# Using the tuple constructor

# fruit_constructor = tuple(('Apple', 'Orange', 'Mango'))

# Get single value

# print(fruit_tuple[1])

# Can not change value

# fruit_tuple[1] = 'Grapes'

# Tuples with one value should have trailing comma

fruit_tuple_2 = ('Grapes',)

# print(fruit_tuple)

# You can't delete individual item, but you can delete it as a hall

del fruit_tuple_2

# print(len((fruit_tuple_2)))

# print(fruit_constructor)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Grapes'}

# check if in set

print('Apple' in fruit_set)

# Add to set

fruit_set.add('Goose')

# Remove to set

fruit_set.remove('Grapes')

# clear set

fruit_set.clear()

# delete set

del fruit_set

print(fruit_set)
