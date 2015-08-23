# -*- coding:utf-8 -*-
class Solution:
    # 判断n是否是s的旋转.
    def LeftRotateString(self, s, n):
        # write code here
        # 判断是否为None
        # if s is None or n is None:
        #     return None
        # # 判断是否为""
        # if s == "" or n < 0:
        #     return None
        if s is None:
            return None
        if s == "":
            return ""
        if n <= 0:
            return s

        n %= len(s)
        #for i in range(len(s)):
        #    if s[i] == key:
        #        tmp = s[i:] + s[:i]
        #        if tmp == n:
        #            return True
        #return False
        s = s[n:] + s[:n]
        return s



so = Solution()
s = "abcdefg"
print so.LeftRotateString(s,2)
print s
