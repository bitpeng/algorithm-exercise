# -*- coding:utf-8 -*-

def MySum(a,i,j): # 求sum = a[i] + a[i + 1] + ...+ a[j]
    if i > j:
        return 0
    s = 0
    for m in range(i, j + 1):
        s += a[m]

    return s

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 0:
            return []
        a = [i for i in range(1, tsum/2 + 2)]
        print a
        i = 0
        j = len(a) - 1
        ret = []
        #while (i < j):
        #    _sumI2J = MySum(a, i, j)
        #    if tsum == _sumI2J:
        #        tmp = a[i:j + 1]
        #        ret.append(tmp)
        #        i += 1
        #        j -= 1
        #    elif tsum > _sumI2J:
        #        i += 1
        #    else:
        #        j -= 1
        for i in range(len(a)):
            j = len(a) - 1
            while (i < j):
                _sumI2J = MySum(a, i, j)
                if tsum == _sumI2J:
                    tmp = a[i:j + 1]
                    ret.append(tmp)
                    i += 1
                    j -= 1
                elif tsum > _sumI2J:
                    i += 1
                else:
                    j -= 1


        return ret

so = Solution()
print so.FindContinuousSequence(100)
