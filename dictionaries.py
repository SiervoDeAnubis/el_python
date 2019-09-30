# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# simple dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# using constructor

# person = dict(first_name = 'John', last_name = 'Doe', age = 30)

# Access Value
print(person['first_name'])

print(person.get('last_name'))

# Add Key/Value

person['phone'] = '1123-4569-7895'

# Get Keys

print(person.keys())

# Get Values

print(person.items())

# Make a  copy

person1 = person.copy()
person1['city'] = 'Boston'

# Remove Item
del(person['age'])
person1.pop('city')

# clear
person1.clear()

# Get Len

print(len(person))

print(person1)

print(person)

# List of dict

people = [
    {'name': 'Marthe', 'age': 30},
    {'name': 'Cesar', 'age': 35}
]

print(people)

print(people[1]['name'])
