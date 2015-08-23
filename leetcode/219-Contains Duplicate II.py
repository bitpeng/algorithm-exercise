'''
Given an array of integers and an integer k, find out whether there there are two distinct indices i 
and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Hide Tags Array Hash Table
Have you met this question in a real interview? Yes  No
Discuss

题目大意：
给定一个整数数组nums与一个整数k，是否存在两个不同的下标i和j满足nums[i] = nums[j]
并且| i - j | <= k。

解题思路：
使用dict保存数组中数字的下标！
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numDict = dict()
        for x in range(len(nums)):
            # 取得每一个数据的下标！
			# dict.get(key), 如果键存在，则返回值；如果key不存在，可以返回None，或者自己指定的value：
            idx = numDict.get(nums[x])
            if idx >= 0 and x - idx <= k:
                return True
            numDict[nums[x]] = x
        return False
        

