# -*- coding:utf-8 -*-
class Solution:
    # 变形要求保存相对顺序
    def reOrderArray(self, a):
        # write code here
        if not a:
            return

        oddList = [i for i in a if i%2]
        evenList = [i for i in a if i%2 == 0]
        a[:] = oddList + evenList
        #int oddLen = len()

    # 变形要求保存相对顺序
    def reOrderArray(self, a):
        # write code here
        if not a:
            return

        oddList = [i for i in a if i%2]
        #evenList = [i for i in a if i%2 == 0]
        #a[:] = oddList + evenList
        int oddLen = len(oddList)
        i = 0
        j = oddLen
        while i < oddLen:
            if i % 2 == 0:
                tmp = a[i]
                a[i:oddLen] = a{i - 1:oddLen - 1}
                a[oddLen - 1] = tmp
                while j < len(a) and a[j]%2 == 0:
                    j -= 1
                if j < len(a):
                    a[oddLen - 1], a[j] == a[j], a[oddLen - 1]

            else:
                i += 1

    # 原题目要求, 只需要奇数在前即可。
    def reOrderArray1(self, a):
        # write code here
        if not a:
            return

        n = len(a)
        i = 0
        j = n - 1
        while i < n and j >= 0 and i <= j:
            while i < n and a[i] % 2:
                i += 1
            while j >= 0 and (a[j] % 2 == 0):
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
            print a, i, j

a = [i for i in range(1, 8)]
print a
s = Solution()
s.reOrderArray(a)
print a
