# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


def sayHello(name='Cecilia'):
    """
    Prints Hello and the name 
    """
    print('Hello ' + name)

# Return Value


def getSume(num1, num2):
    total = num1 + num2
    return total


print(getSume(1, 2))


def addOneToNum(num):
    num = num + 1
    # num += 1
    return num


print(addOneToNum(3))
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


def getSum(num1, num2): return num2 + num1

# getsum = lambda num1, num2 : num1 + num2


def addOneToNumLambda(num): return num + 1


print(getSum(9, 1))

print(addOneToNumLambda(3))
