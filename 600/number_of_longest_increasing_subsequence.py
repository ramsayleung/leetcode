"""
source: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
author: Ramsay Leung
date: 2020-02-26

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int. 
"""
from typing import List

# intuition: dynamic programming
# X X X j X i
# if i > j, lis[i] < lis[j] + 1, then nils[i] = nils[j]
# if i > j, lis[i] = lis[j] + 1, means has another road to i resulting in the same lis, then nils[i] += nils[j]
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return len(nums)
        lis = [1] * len(nums)
        nlis = [1] * len(nums)
        for x in range(len(nums)):
            for p in range(x):
                if nums[p] < nums[x]:
                    if lis[p] + 1 > lis[x]:
                        lis[x] = lis[p] + 1
                        nlis[x] = nlis[p]
                    elif lis[p] + 1 == lis[x]:
                        nlis[x] += nlis[p]
        maxLIS = max(lis)
        return sum([nlis[i] for i, x in enumerate(lis) if x == maxLIS])
