# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n:
            return 0
        if n <= 0:
            return 0

        cnt = 0
        for i in range(1,n + 1):
            s = unicode(i)
            cnt += s.count('1')

        return cnt

    def NumberOf1Between1AndN_Solution_2(self, n):
        # write code here
        if not n:
            return 0
        if n <= 0:
            return 0

        cnt = 0
        for i in range(1,n + 1):
            s = unicode(i)
            #cnt += s.count('1')
            for i in s:
                if i == '1':
                    cnt += 1

        return cnt

import time
import random
s = Solution()
t1 = time.time()

print s.NumberOf1Between1AndN_Solution(1234568)
t2 = time.time()
print s.NumberOf1Between1AndN_Solution_2(1234568)
t3 = time.time()

print t2 - t1
print t3 - t2
