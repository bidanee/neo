#!/usr/bin/env python

# def gcd():
#     a = int(input('input number a : '))
#     b =  int(input('input number b :'))
#     while True:
#             r = b % a
#             b = a
#             a = r
#             return a
# print(gcd())

def gcd(a,b):
    print('gcd',(a,b))
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

a = int(input('Input First number : '))
b = int(input('Input Second number : '))

print(f'gcd({a},{b}) = {gcd(a,b)}')


