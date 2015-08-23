'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Hide Tags Array Hash Table
Have you met this question in a real interview? Yes  No
Discuss

'''

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        num_dict = dict()
        for x in xrange(len(nums)):
            idx = num_dict.get(nums[x])
            if idx is not None:
                return True
            else:
                num_dict[nums[x]] = x
                
        return False
        