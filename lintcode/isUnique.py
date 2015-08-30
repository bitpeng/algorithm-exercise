#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
   判断字符串是否没有重复字符

   43% 通过
   实现一个算法确定字符串中的字符是否均唯一出现
   
   您在真实的面试中是否遇到过这个题？ Yes
   样例
   给出"abc"，返回 true
   
   给出"aab"，返回 false
   
   挑战
   如果不使用额外的存储空间，你的算法该如何改变？ 
'''

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        # d = {}
        if str is None:
            return False
        if not str:
            return True

        l = []
        for i in str:
            if i in l:
                return False
            else:
                l.append(i)
        return True

