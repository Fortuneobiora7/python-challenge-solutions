'''
4. Write a Python program to test whether a passed letter is a vowel or not.
'''

def check_vowel(char):
    vowels = 'aeiou'
    return char in vowels
print(check_vowel('z'))
print(check_vowel('i'))