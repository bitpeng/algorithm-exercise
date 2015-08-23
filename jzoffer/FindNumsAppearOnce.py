# -*- coding:utf-8 -*-
'''
题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

'''
>>> import random;li = [random.randint(0,5) for i in range(15)]
>>> c = Counter(li)
>>> c
Counter({4: 5, 0: 4, 1: 3, 5: 2, 2: 1})
>>> c.most_common()
[(4, 5), (0, 4), (1, 3), (5, 2), (2, 1)]
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        from collections import Counter
        if not array or len(array) < 2:
            return [0,0]
        c = Counter(array)
        most_two = c.most_common()[:-3:-1]
        ret = []
        for i in most_two:
            ret.append(i[0])
            
        return ret