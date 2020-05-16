'''
6. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
    Tools: abs function, input function, math
'''

#import math

#x=int(input())
number = int(input('Enter an integer: '))

diff = number-17

if number>17:
    print((abs(diff)*2))


