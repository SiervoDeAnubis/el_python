# Python has functions for creating, reading, updating, and deleting files.

# open a file

myFile = open('myfile.txt', 'w')  # write

# Get Some info

print('Name: ', myFile.name)
print('IsClosed: ', myFile.closed)
print('Openning Mode: ', myFile.mode)

# Write to file

myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

# Append to File

myFile = open('myfile.txt', 'a')  # append
myFile.write(' I also like PHP')
myFile.close()

# Read from File

myFile = open('myfile.txt', 'r+')  # read
text = myFile.read(10)
print(text)
