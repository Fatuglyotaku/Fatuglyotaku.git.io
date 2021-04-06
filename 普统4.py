# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:33:58 2021

@author: Zhang_Weihan
"""

"""
Monte Carlo
"""

import random

times = 10000

cnt = 0

for i in range(times):
    
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    X = x1 + x2
    
    if X == 3:
        cnt += 1

print(cnt/times)

import random

times = 10000

cnt = 0

for i in range(times):
    
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    x3 = random.randint(1, 6)
    x4 = random.randint(1, 6)
    x5 = random.randint(1, 6)
    
    if x1 == x2 == x3 == x4 == x5:
        cnt += 1

print(cnt/times)

import random

times = 10000

cnt = 0

for i in range(times):
    
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    x3 = random.randint(1, 6)
    x4 = random.randint(1, 6)
    x5 = random.randint(1, 6)
    
    if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x2 != x3 and x2 != x4 and x2 != x5 and x3 != x4 and x3 != x5 and x4 != x5:
        cnt += 1

print(cnt/times)

import random

times = 10000

cnt = 0

for i in range(times):
    
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    x3 = random.randint(1, 6)
    x4 = random.randint(1, 6)
    x5 = random.randint(1, 6)
    
    if (x1 == x2 == x3 == x4 and x1 != x5) or (x1 == x2 == x3 == x5 and x1 != x4) or (x1 == x2 == x4 == x5 and x1 != x3) or (x2 == x3 == x4 == x5 and x2 != x1) or (x1 == x3 == x4 == x5 and x1 != x2):
        cnt += 1

print(cnt/times)

import random

times = 10000

cnt = 0

for i in range(times):
    
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    x3 = random.randint(1, 6)
    x4 = random.randint(1, 6)
    x5 = random.randint(1, 6)
    
    if (x1 == x2 == x3 and x4 == x5 and x1 != x5) or (x1 == x2 == x4 and x3 == x5 and x1 != x5) or (x1 == x2 == x5 and x3 == x4 and x1 != x4) or (x1 == x4 == x5 and x2 == x3 and x1 != x3) or (x1 == x3 == x5 and x2 == x4 and x1 != x4) or (x1 == x3 == x4 and x2 == x5 and x1 != x5) or (x2 == x3 == x4 and x1 == x5 and x2 != x5) or (x2 == x3 == x5 and x1 == x4 and x2 != x5) or (x2 == x4 == x5 and x1 == x3 and x2 != x3) or (x3 == x4 == x5 and x1 == x2 and x3 != x1):
        cnt += 1

print(cnt/times)