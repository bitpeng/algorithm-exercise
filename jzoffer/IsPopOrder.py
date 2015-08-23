# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        s = []  # 辅助栈
        k = 0
        for item in pushV:
            s.append(item)
            while s and s[-1] == popV[k]:
                s.pop()
                k += 1
        return len(s) == 0


