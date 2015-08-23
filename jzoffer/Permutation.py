# -*- coding:utf-8 -*-
'''
题目描述

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。 
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        from itertools import permutations
        s = permutations(ss)
        ret = []
        # >>> a = permutations('aba');b = list(a)
        # >>> b
        # [('a', 'b', 'a'), ('a', 'a', 'b'), ('b', 'a', 'a'), ('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a')]
        # >>> 
        # 所以这里需要去除重复的，而不能仅仅是return list(s)
        for i in s:
            s = ''.join(i)
            if s in ret:
                pass
            else:
                ret.append(s)
        return ret