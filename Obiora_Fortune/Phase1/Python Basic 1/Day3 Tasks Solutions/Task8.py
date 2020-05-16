'''
8. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
    Tools: math, input function
'''

import math
x=int(input('Enter the first number: '))
y=int(input('Enter the second number: '))
z=int(input('Enter the third number: '))

sum = x+y+z

if x is y is z:
    print(sum*3)