"""
source: https://leetcode.com/problems/minimum-path-sum/
author: Ramsay Leung
date: 2020-03-26
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""
# dp[y][x] = min(dp[y-1][x], dp[y][x-1])+grid[y][x]
# when y = 0, dp[0][x] = dp[0][x-1]+grid[0][x]
# when x = 0, dp[y][0] = dp[y-1][0]+grid[y][0]
from typing import List


# time complxity: O(m*n), the size of 2d array `grid` is m*n
# space complxity: O(m*n), the size of 2d array `grid` is m*n
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ylen = len(grid)
        xlen = len(grid[0]) if ylen > 0 else 0
        dp = [[0 for i in range(xlen)] for i in range(ylen)]
        for y in range(ylen):
            dp[y][0] = dp[y-1][0]+grid[y][0] if y > 0 else grid[y][0]
            for x in range(xlen):
                if y == 0:
                    dp[0][x] = dp[0][x-1]+grid[0][x] if x > 0 else grid[0][x]
                elif x > 0 and y > 0:
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + grid[y][x]
        return dp[ylen-1][xlen - 1]
