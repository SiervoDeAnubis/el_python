# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'cesar', 'cecilia', 'ana']

for person in people:
    print('Current person: ', person)

# Break out loop

for person in people:
    print('current person: ', person)
    if person == 'cecilia':
        break

# the position of the break it really matters

# Continue

for person in people:
    if person == 'cecilia':
        continue
    print('current person: ', person)

# Range

for i in range(len(people)):
    print(f'Current person: -> {people[i]}')

for i in range(0, 10):
    print(f'Number: {i}')
# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print('Count: ', count)
    count += 1
