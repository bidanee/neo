#!/usr/bin/env python

import prime_func

while True:
    n = int(input("Input the number(0:quit) : "))
    if (n == 0):
        break
    if (n < 2) :
        print('re-enter number~!!')
        continue
    print(f'{n} is prime number') if prime_func.prime(n)==1 else print('re-enter number~!!')


