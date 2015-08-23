'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if not len(num):
            return 0
        ret = num[0] + num[1] + num[2]
        num.sort()
        for i in range(len(num) - 2):
            j = i + 1
            k = len(num) - 1
            while j < k:
                tsum = num[i] + num[j] + num[k]
                if abs(tsum - target) < abs(ret - target):
                    ret = tsum
                if tsum < target:
                    j += 1
                elif tsum > target:
                    k -= 1
                else:
                    j += 1
                    k -= 1
        return ret