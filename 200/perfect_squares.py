"""
source: https://leetcode.com/problems/perfect-squares/ 
author: Ramsay Leung
date: 2020-03-31
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

from bisect import bisect_right
from math import sqrt


# time complxity: O(n*sqrt(n)), n is the length of `n`
# space complxity: O(n), n is the length of `n`
class Solution:
    def numSquares(self, n: int) -> int:
        perfactSquares = [x**2 for x in range(1, int(sqrt(n)) + 1)]
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            # Find rightmost value less than or equal to i in a sorted list
            index = bisect_right(perfactSquares, i)
            dp[i] = min([dp[i - perfactSquares[j]] for j in range(index)]) + 1
        return dp[n]