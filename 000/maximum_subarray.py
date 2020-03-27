"""
source: https://leetcode.com/problems/maximum-subarray/
author: Ramsay Leung
date: 2020-03-25

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
# time complxity: O(n), n is the length of nums
# space complxity: O(1)
from sys import maxsize
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        result = -maxsize + 1
        for i in nums:
            currentSum = max(currentSum+i, i)
            result = max(result, currentSum)
        return result
