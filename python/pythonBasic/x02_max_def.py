#!/usr/bin/env python

import random

data = random.sample(range(1,101), 10)

def maxNumber(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

print(data)
print(f'Max value is {maxNumber(data)}')

def maxNumber2(numbers):
    max = numbers
    for num in range(len(numbers)):
        if numbers[num] > max:
            max = numbers[num]
    return max
print(data)
print(f'Max value is {maxNumber(data)}')