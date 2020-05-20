'''
6. Write a Python program to add two objects if both objects are an integer type.
'''


def to_add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        print(x + y)
    return 'Please enter integer values'
print(to_add(3, 4))

