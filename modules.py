# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date
import time

from validator import validate_email
# from camelcase import CamelCase

# PIP Modules

today = datetime.date.today()
print(today)


timestamp = time.time()

print(timestamp)

# camel = CamelCase()
# text = 'hello world!!!!'

# print(camel.hump(text))

email = 'cesar.espiritu@globant.com'

if validate_email(email):
    print('emails is valid')
else:
    print('no valid email')
