'''
7. Write a Python program to display your details like name, age, address in three different lines.
'''

def my_details():
    name = input('Enter name: ')
    age = input('Enter age: ')
    address = input('Enter address: ')
    print('Name: {} \nAge: {} \nAddress: {}'.format(name, age, address))

my_details()