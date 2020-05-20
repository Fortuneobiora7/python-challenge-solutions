'''
5. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
def check_value(group_data, n):
    for x in group_data:
        if n == x:
            return True
    else:
        return False
print(check_value([1,5,8,3], 3))
print(check_value([1,5,8,3], -1))
