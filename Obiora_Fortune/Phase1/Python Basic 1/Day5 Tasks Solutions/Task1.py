'''
1. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''

def gcd(x, y):
    gcd=1
    if x % y == 0:
        return y
    for i in range(int(y/2), 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break;
    return gcd

print(gcd(12, 4))
print(gcd(16, 64))
