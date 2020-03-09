'''
source: https://leetcode.com/problems/maximum-average-subarray-ii/
author: Ramsay Leung
date: 2020-03-09
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.

Note:

    1 <= k <= n <= 10,000.
    Elements of the given array will be in range [-10,000, 10,000].
    The answer with the calculation error less than 10-5 will be accepted.
'''
from typing import List


# time complexity: O(N*log(max-min)), N is the length of nums, max is the maximum element in nums, and min is the minimum element in nums.
# space complexity: O(N), N is the length of nums
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numsLen = len(nums)
        right = max(nums)
        left = min(nums)
        differenceSum = [0] * (numsLen + 1)
        while (right - left) > 1e-5:
            minDifferenceSum = 0
            mid = (right + left) / 2
            check = False
            for i in range(1, numsLen + 1):
                differenceSum[i] = differenceSum[i - 1] + (nums[i - 1] - mid)
                if i >= k:
                    minDifferenceSum = min(minDifferenceSum,
                                           differenceSum[i - k])
                    if differenceSum[i] - minDifferenceSum > 0:
                        check = True
                        break
            if check:
                left = mid
            else:
                right = mid
        return left
