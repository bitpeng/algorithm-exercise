#coding:utf-8
'''
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place, do not allocate extra memory.
    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
'''

# '''
# 我们知道c++STL中有个函数next_permutation,这个函数时求某个排列的下一个大的排列。所谓的下一个
# 大的排列可以如下解释：如果把数组元素看成是某个字符，这些字符组成一个字符串，下一个大的排列就
# 是比当前排列代表的字符串更大（按字典序比较），且不存在介于两个字符串之间的字符串。例如对于字符串abc，
# 它的下一个大排列是acb。

# 对于某个排列，我们如下求它的下一个大的排列：

# 从最尾端开始往前寻找两个相邻的元素，两者满足i < ii（令第一个元素为i，第二个元素为ii）
# 如果没有找到这样的一对元素则，表明当前的排列是最大的，没有下一个大的排列
# 如果找到，再从末尾开始找出第一个大于i的元素，记为j
# 交换元素i, j，再将ii后面的所有元素颠倒排列(包括ii)
# 按照的STL实现，如果某个排列没有比他大的下一个排列，调用这个函数还是会把原排列翻转，即得到最小的排列
# '''

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = nums
        L = len(n)
        i = L - 2
        ii = L - 1
        while(i >= 0):
            if n[i] < n[ii]:
                break
            else:
                i -= 1
                ii -= 1
        if i < 0:
            nums.reverse()
            return

        j = L - 1
        while(True):
            if n[j] > n[i]:
                break;
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]
        # 注意这里最大的陷进，由于要求原地赋值，这种方式不可行！特别注意。
        #nums = nums[:ii] + list(reversed(nums[ii:]))
        nums[:] = nums[:ii] + list(reversed(nums[ii:]))


