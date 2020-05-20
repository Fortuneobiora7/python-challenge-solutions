'''
4. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''

x = int(input('Enter first integer: '))
y = int(input('Enter second integer: '))
def sum(x, y):
    sum = int(x + y)
    if 15<sum<20:
        sum = 20
    return sum

print(sum(x,y))
#print(sum(10,7))