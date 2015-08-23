'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
Hide Tags Array Backtracking
Have you met this question in a real interview? Yes  No
Discuss

'''

class Solution:
    # @param {integer[]} candidates, C
    # @param {integer} target, T
    # @return {integer[][]}
    res = []
    def combinationSum(self, C, T):
        
        C.sort()
        tmpres = []
        helper(C, 0, T, tmpres)
        return self.res
        
    def helper(self, C, index, T, tmpres):
        if T == 0:
            self.res.append(tmpres)
            return
        
        i = index
        while i < len(C):
            if i == 0 or C[i] != C[i - 1]
                tmpres.append(C[i])
                helper(C, i, T - C[i], tmpres)
                tmpres.pop()
            
            i += 1
        
        
        
        
        
        
        
        
        
        