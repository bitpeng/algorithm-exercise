#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from random import randint
import time

def LIS(a):
    if not a:
        return 0

    dp = [1 for i in a]   # len(a) = n
    n = len(a)
    for i in range(n):       # i = 0, 1, 2....n - 1
        for j in range(i):   # j = 0, 1, 2... i - 1
            if a[i] >= a[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)

a = [1,1,2,-3,4,-5,6,-7]
for i in range(10):
    a = [randint(1,20) for i in range(10)]
    print a
    print LIS(a)
    print 
    time.sleep(1)




