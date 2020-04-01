"""
source: https://leetcode.com/problems/integer-break/
author: Ramsay Leung
date: 2020-04-01
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.

"""

# time complexity: O(n**2)
# space complexity: O(n)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i - j] * j, (i - j) * j, dp[i])
        return dp[n]
