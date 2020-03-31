"""
source: https://leetcode.com/problems/longest-increasing-subsequence/
author: Ramsay Leung
date: 2020-03-31

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""

from typing import List


# xxxxx i dp[i] = dp[j] + 1 if nums[i]>nums[j]
# time complxity: O(n**2), n is the length of `nums`
# space complxity: O(n), n is the length of `nums`
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        dp = [1] * (length + 1)
        lis = 1  # longest increasing subsequence
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:  # it means dp[i] is unset
                        dp[i] = dp[j] + 1
            lis = max(dp[i], lis)
        return lis