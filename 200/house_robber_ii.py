"""
source: https://leetcode.com/problems/house-robber-ii/
author: Ramsay Leung
date: 2020-03-29

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
from typing import List


# xxxxx i dp[i]= max(dp[:i-1)] + nums[i] and if i == len-1, you cannot rob house[0]
# e.g. max(dp[:i-1]) cannot contains nums[0]
# maxAmount = max(dp[i],maxAmount)
# time complexity: O(n), n is the length of `nums`
# space complexity: O(n), n is the length of `nums`
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        circleDp = [0] * size
        return max(self.iterate(list(range(size-1)), dp, nums), self.iterate(list(range(1, size)), circleDp, nums))

    def iterate(self, _range: List[int], dp: List[int], nums: List[int]) -> int:
        maxAmount = 0
        for i in _range:
            if i == 0 or i == 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[:i-1])+nums[i]
            if dp[i] > maxAmount:
                maxAmount = dp[i]
        return maxAmount
