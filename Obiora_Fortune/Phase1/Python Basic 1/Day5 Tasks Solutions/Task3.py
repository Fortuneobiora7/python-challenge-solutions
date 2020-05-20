'''
3. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''

x = int(input('Enter first value: '))
y = int(input('Enter second value: '))
z = int(input('Enter third value: '))
sum = x+y+z
if (x == y) or (x == z) or (y == z):
    print(0)
else:
    print(sum)