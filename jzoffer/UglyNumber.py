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

print isUglyNumber(6)

# for i in range(2, 100):
#     # print i
#     if isUglyNumber(i):
#         print i

# class Solution:
#     def UglyNumberList(self):
#         for i in itertools.count(1):
#             if self.UgleNumber(i):
#                 yield i
#     def GetUglyNumber_Solution(self, index):
#         # write code here
#         return UglyNumberList[index]
#

# print UglyNumberList()[10]

for i in UglyNumberList():
    print i
    time.sleep(0.1)
