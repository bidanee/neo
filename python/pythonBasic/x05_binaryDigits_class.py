#!/usr/bin/env python

import random

class BinaryDigits(object):
    def __init__(self, n,lists):
        self.n = n
        self.lists = lists
    def convert(self):
        q = self.n
        while True:
            r = q % 2
            q = q // 2
            lists.append(r)
            if q == 0:
                break
        lists.reverse()
        return lists


lists = []
num = random.randrange(4, 20)
binary = BinaryDigits(num,[])
print(f'{num} binary number is {binary.convert()}')