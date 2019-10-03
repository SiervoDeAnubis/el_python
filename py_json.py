# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample Json

userJSON = '{"first_name": "John", "last_name" : "Zas", "age": 30}'

# Parse to dict

user = json.loads(userJSON)

print(user)
print(user['first_name'])


car = {'make': 'ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)
