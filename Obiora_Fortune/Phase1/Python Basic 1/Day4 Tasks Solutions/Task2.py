'''
2. Write a Python program to count the number 4 in a given list.
'''


def count_func(nums):
    count = 0
    for num in nums:
        if num ==4:
            count = count + 1
    return count

print(count_func([4,5,6,4,4,5,4]))