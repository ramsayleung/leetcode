"""
source: https://leetcode.com/problems/house-robber/
date: 2020-03-29
author: Ramsay Leung

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


"""

# xxxxx i dp[i]= max(dp[:i-1)] + i
# maxAmount = max(dp[i],maxAmount)
from typing import List


# time complexity: O(n), n is the number of `nums`
# space complexity: O(n), n is the number of `nums`
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size
        maxAmount = 0
        for i in range(size):
            if i == 0 or i == 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[:i-1]) + nums[i]
            maxAmount = max(dp[i], maxAmount)
        return maxAmount
