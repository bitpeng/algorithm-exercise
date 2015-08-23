# -*- coding:utf-8 -*-
import itertools
import time

# 假如一个数是丑数，那么不断经过2,3,5整除后会为0.
# 假如不是，比如7不是丑数，那么循环一轮之后，n还是7.那么可以判断它不是丑数。
def isUglyNumber(n):
    if not n:
        return False
    last = n # 记录上一次循环的n值.
    while n:
        # print 'test:', n
        if n <= 5:
            return True
        if n % 2 == 0:
            n = n/2
        if n % 3 == 0:
            n = n/3
        if n % 5 == 0:
            n = n/5
        if last == n:
            return False
        else:
            last = n

    return True

def UglyNumberList():
    for i in itertools.count(1):
        if isUglyNumber(i):
            yield i

class Solution:
    # def UgleNumber(self, i):
    #     if i == 1:
    #         return True
    #     while i >= 2: #and not i in [2,3,5]:
    #         i = i%5 if i % 5 == 0 else i
    #         i = i%3 if i % 3 == 0 else i
    #         i = i%2 if i % 2 == 0 else i
    #     if i in [0, 2, 3, 5]:
    #         return True
    #     else: return False

    # def UglyNumberList(self):
    #     for i in itertools.count(1):
    #         if self.UgleNumber(i):
    #             yield i

    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index:
            return None
        if index <= 0:
            return None
        k = 1
        for i in UglyNumberList():
            if k == index:
                return i
            else:k += 1

t = time.time()

s = Solution()
for i in range(500, 501):
    print s.GetUglyNumber_Solution(i)

print time.time() - t
