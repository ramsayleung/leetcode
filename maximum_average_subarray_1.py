'''
source: https://leetcode.com/problems/maximum-average-subarray-i/
author: Ramsay Leung
date: 2020-03-08
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

 

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
'''

# time complexity: O(N), N is the length of `nums`
# space complexity: O(N), N is the length of `nums`
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = _max = sum(nums[0:k])
        numsLen = len(nums)
        for i in range(1, numsLen - k + 1):
            _sum = _sum - nums[i - 1] + nums[k + i - 1]
            if _sum > _max:
                _max = _sum
        return _max / k