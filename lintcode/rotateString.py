#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
    旋转字符串

    22% 通过
    给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

    您在真实的面试中是否遇到过这个题？ Yes
    样例
    对于字符串 "abcdefg".

    offset=0 => "abcdefg"
    offset=1 => "gabcdef"
    offset=2 => "fgabcde"
    offset=3 => "efgabcd"
    挑战
    在数组上原地旋转，使用O(1)的额外空间
'''

def reverse(s, i, j): # 翻转s[i...j](闭区间)为s[j....i]
    if not s or i < 0 or j < 0 or i >= j:
        return
    b = i; e = j;
    while b < e:
        s[b], s[e] = s[e], s[b]
        b +=1 ; e -= 1

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if not s or offset < 0:
            return 
        offset = offset % len(s)
        reverse(s, 0, offset)
        reverse(s, offset + 1, len(s) - 1)
        reverse(s, 0, len(s) - 1)

so = Solution()
s = "abcdefg"
s = list(s)
so.rotateString(s, 3)
print s
