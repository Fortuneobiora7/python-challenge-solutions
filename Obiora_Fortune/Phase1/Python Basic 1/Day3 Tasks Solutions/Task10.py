'''
10. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
    Tools: input function, slicing
'''

def my_func(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result
print(my_func('Hello', 5))