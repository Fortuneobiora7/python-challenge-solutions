'''
6. Write a Python program to create a histogram from a given list of integers.
'''

def histogram(values):
    for n in values:
        output = ''
        x = n
        while(x > 0):
            output += '*'
            x = x - 1
        print(output)

histogram([1,2,3,4,5,6])