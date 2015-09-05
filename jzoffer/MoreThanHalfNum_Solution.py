# -*- coding:utf-8 -*-
'''
    题目描述
    
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
    
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        from collections import Counter
        c = Counter(numbers)
        m = c.most_common(1)[0]
        if m[1] > len(numbers) / 2:
            return m[0] 
        else: return 0
