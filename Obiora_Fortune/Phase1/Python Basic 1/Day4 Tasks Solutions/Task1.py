'''
1. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
'''

num = int(input('Enter number: '))
rem = num % 2
if rem > 0:
    print('This is an odd number.')
else:
    print('This is an evil number.')