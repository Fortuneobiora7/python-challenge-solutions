'''
3. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
'''

def my_func(str, n):
    x = 2
    if x > len(str):
        x = len(str)
    y = str[:x]
    result = ''
    for i in range(n):
        result = result + y
    return result

print(my_func('Hello', 3))
print(my_func('H', 4))