'''
1. Write a Python program to check whether a file exists.
'''

import os.path

open('KPMG_VI_New_raw_data_update_final.xlsx', 'r')
print(os.path.isfile('KPMG_VI_New_raw_data_update_final'))