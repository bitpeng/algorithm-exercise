'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Hide Tags Divide and Conquer Array Binary Search
用二分的思路去做，这不好想，还要考虑到奇偶。可以转化思维，去求两个有序数组中的第 K 大数，这样就比较好想了。
'''

'''
Input: # 从这个例子可以看出，对于偶数个数组，中位数是中间两个的平均值！
[], [2,3]
Output:
null
Expected:
2.50000
'''

class Solution:
    #寻找有序数组A，B中第k大的数！
    def findKthSortedArrays(self, A, B, k):
        if len(A) < len(B):
            tmp = A
            A = B
            B = tmp
        # 如果B为空。
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pb = min(k / 2, len(B))
        pa = k - pb
        if A[pa - 1] > B[pb - 1]:
            return self.findKthSortedArrays(A, B[pb:], k - pb)
        elif A[pa - 1] < B[pb - 1]:
            return self.findKthSortedArrays(A[pa:], B, k - pa)
        else:
            return A[pa - 1]

    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (len(A) + len(B)) % 2 == 1:
            return self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2 + 1)
        #else:
            return (self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2) +
                self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2 + 1)) / 2.0
