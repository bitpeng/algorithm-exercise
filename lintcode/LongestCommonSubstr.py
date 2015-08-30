#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random
import time

'''
def LongestPrefix(s1, s2):
    if not s1 or not s2:
        return 0, ""
    i = 0
    n1 = len(s1); n2 = len(s2)
    while i < n1 and i < n2 and s1[i] == s2[i]:
        i += 1
    return i, s1[:i]
'''

''' 求最长重复子串，思路:
    前面提过后缀数组的基本定义，与子串有关，可以尝试这方面思路。由于后缀数组最典型的是寻找一个字
    符串的重复子串，所以，对于两个字符串，我们可以将其连接到一起，如果某一个子串s是它们的公共子串，
    则s一定会在连接后字符串后缀数组中出现两次，这样就将最长公共子串转成最长重复子串的问题了，这里的
    后缀数组我们使用基本的实现方式。

    值得一提的是，在找到两个重复子串时，不一定就是X与Y的公共子串，也可能是X或Y的自身重复子串，故在连
    接时候我们在X后面插入一个特殊字符‘#’，即连接后为X#Y。这样一来，只有找到的两个重复子串恰好有一个
    在#的前面，这两个重复子串才是X与Y的公共子串。
'''
t = time.time()
def LongestPrefix_2(s1, s2):
    if not s1 or not s2:
        return 0, ""
    if '#' in s1 and '#' in s2: # 他们的后缀不能来自于同一个串
        return 0,""
    if '#' not in s1 and '#' not in s2:
        return 0, ""
    i = 0
    n1 = len(s1); n2 = len(s2)
    while i < n1 and i < n2 and s1[i] == s2[i]:
        i += 1
    return i, s1[:i]

def LongestRepeatSubstring(s):
    if not s:
        return ""
    a = [s[i:] for i in range(len(s))]
    a.sort()
    ret = 0; retstr = ""
    for i in range(len(a) - 1):
        tmp, substr = LongestPrefix_2(a[i], a[i + 1])
        if tmp > ret:
            ret = tmp; retstr = substr
    return ret, retstr

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        s = A + "#" + B
        ret, retstr = LongestRepeatSubstring(s)
        return ret, retstr

so = Solution()
print so.longestCommonSubstring("abcdefcdefcd", "cdef")



#print LongestRepeatSubstring("abcdefcdef")
#print LongestRepeatSubstring("abcdefcdefc")
#print LongestRepeatSubstring("abcdefcdefcd")
#s = ''.join([chr(random.randint(97, 105)) for i in range(5000)])
##print s
#print LongestRepeatSubstring(s)
#print time.time() - t
