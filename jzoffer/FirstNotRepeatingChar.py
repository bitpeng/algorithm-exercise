# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        from collections import OrderedDict
        if not s:
            return -1

        # 以字符作为键, 以出现次数作为值
        d = OrderedDict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # print d
        # 把第一次出现一次的字符记录下来
        k = None
        for i in d:
            if d[i] == 1:
                # print i
                k = i
                break
        # print 'k: ', k
        if k is None:
            return -1
        for i in range(len(s)):
            print s[i], k
            if s[i] == k:
                return i
        return None

so = Solution()
print so.FirstNotRepeatingChar('google')
print so.FirstNotRepeatingChar('aabccdbd')
#print c
