"""
source: https://leetcode.com/problems/non-decreasing-array/
author: Ramsay Leung
date: 2020-03-01
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        isDescrsasing = False
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            if nums[i] > nums[i + 1]:
                tmp = nums[i]
                del nums[i]
                if not self.isIncreasing(nums):
                    nums.insert(i, tmp)
                    del nums[i + 1]
                    return self.isIncreasing(nums)
                else:
                    return True
        return True

    def isIncreasing(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            if nums[i] > nums[i + 1]:
                return False
        return True
