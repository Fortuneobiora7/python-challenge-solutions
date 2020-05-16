'''
9. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
    Tools: input function, string formating
'''

def my_string(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    return 'Is' + str
print(my_string('Is Hello'))