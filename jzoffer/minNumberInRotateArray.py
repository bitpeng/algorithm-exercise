# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, A):
        # write code here
        i = 0
        j = len(A) - 1
        mid = 0
        while A[i] >= A[j]:
            if j - i == 1:
                return A[mid]
            mid = (i + j) / 2

