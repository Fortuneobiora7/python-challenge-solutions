'''
7. Write a Python program to test whether a number is within 100 of 1000 or 2000.
    Tools: maths,input function
'''

Number = int(input('Number: '))
def within(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <= 100))

print(within(Number))