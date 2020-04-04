"""
source: https://leetcode.com/problems/combination-sum-iv/ 
author: Ramsay Leung
date: 2020-04-04
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
1. What if negative numbers are allowed in the given array?
2. How does it change the problem?
3. What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""
from typing import List


# time complexity O(n*m), n is the size of `target`, m is the length of `nums`
# time complexity O(n), n is the size of `target`, m is the length of `nums`
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        size = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
        return dp[target]
