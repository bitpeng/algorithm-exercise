# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        m = len(array) # 行
        n = max([len(i) for i in array]) # 列大小
        # for i in xrange(m):
        #     # for j in xrange(n):
        #     # if
        #     if len(array[i]) == n:
        #         pass
        #     else:
        #         for i in xrange(len(array[i]), n):
        #             array[i].append(None)
        i = 0
        j = n - 1
        while 0 <= i < m and 0 <=j < n:
            print array[i][j]
            if array[i][j] is None:
                continue
            elif array[i][j] == target:
                return True
            elif array[i][j] < target:
                i = i + 1
            else:
                j = j - 1
        return False

s = Solution()
l = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print s.Find(l, 7)
