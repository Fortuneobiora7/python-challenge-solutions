'''
4. Write a Python program to calculate number of days between two dates.
        Sample dates : (2014, 7, 2), (2014, 7, 11)
        Expected output : 9 days
    Tools: Datetime module, timedelta module
'''

import datetime
x=datetime.datetime(2014, 7, 2)
y=datetime.datetime(2014, 7, 11)
print(y-x)