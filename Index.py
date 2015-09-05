#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from random import randint

# a为无序数组，求key在a中的位次。
# 如 a = [3, 2, 4, 5, 1], k = 4, 则位次为2. k 是数组中第二大元素！
def Index(a, k):
    #if not a or not k: return -1
    cnt = 0
    for i in a:
        if i > k: cnt += 1
    return cnt + 1

for i in range(10):
    a = [randint(0, 10) for i in range(11)]
    b = a.pop()
    print a, b, 
    print Index(a, b)
    print 
