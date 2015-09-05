#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def LongestContinousSubArr(a):
    if not a: return 0
    curMax = 1; retMax = 1
    endIndex = 0
    for i in range(1, len(a)):
        if a[i] == a[i - 1] + 1:
            curMax += 1
            #endIndex += 1
        else: curMax = 1; #endIndex = i
        if curMax > retMax:
            retMax = curMax
            endIndex = i

    #print "endIndex", endIndex
    return retMax, a[endIndex + 1 - retMax: endIndex + 1]

def Test_LongestContinousSubArr():
    a = [1, 3, 4, 5, 6, 9, 10]
    b = a + [11, 12, 13, 14]
    print a, LongestContinousSubArr(a)
    print b, LongestContinousSubArr(b)

Test_LongestContinousSubArr()
