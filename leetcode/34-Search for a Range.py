'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, n, target):
        if len(n) == 0:
            return [-1, -1]
        L = len(n)
        M = L / 2
        i = 0
        j = L - 1
        s = e = -1
        while i <= j:
            M = (i + j) / 2
            if n[M] == target:
                s = e = M
                while 0 <= s < L:
                    if n[s] == target:
                        s -= 1
                    else:break
                s += 1
                
                while 0 <= e < L:
                    if n[e] == target:
                        e += 1
                    else:break
                e -= 1  
                break
                pass
            elif n[M] < target:
                i = M + 1
            else:
                j = M - 1
        return [s, e]
        
s = Solution()
a = [5, 7, 7, 8, 8, 10]
print s.searchRange(a, 8)

