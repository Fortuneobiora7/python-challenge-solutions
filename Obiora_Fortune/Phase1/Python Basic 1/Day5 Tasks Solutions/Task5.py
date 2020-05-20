'''
5. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

x = int(input('Enter first integer: '))
y = int(input('Enter second integer: '))
sum = x + y
diff = abs(x - y)
def my_func(x, y):
    if x == y or sum == 5 or diff == 5:
        return True
    else:
        return False
print(my_func(x, y))