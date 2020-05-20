'''
9. Write a Python program to list all files in a directory in Python.
'''

from os import listdir
from os.path import isfile, join
list_files = [f for f in listdir('C:\\Users\\fortune\Desktop\Hash Analytics\KPMG\Day6 Tasks Solutions')]
print(list_files)