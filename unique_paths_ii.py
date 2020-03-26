"""
source: https://leetcode.com/problems/unique-paths-ii/
author: Ramsay Leung
date: 2020-03-26

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


"""
# dp[y][x] = dp[y][x-1] + dp[y-1][x]
# dp[0][x] = 1 dp[y][0] = 1
# obstacle[yo][xo] = dp[yo][xo] = 0
from typing import List


# time complxity: O(m*n)
# space complxity: O(m*n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ylen = len(obstacleGrid)
        xlen = len(obstacleGrid[0]) if len(obstacleGrid) > 0 else 0
        dp = [[-1 for i in range(xlen)]for i in range(ylen)]
        for y in range(ylen):
            if dp[y][0] == -1:
                dp[y][0] = 1
            for x in range(xlen):
                if dp[0][x] == -1:
                    dp[0][x] = 1
                if obstacleGrid[y][x] == 1:
                    for i in range(y, ylen):
                        dp[i][x] = 0
                    for i in range(x, xlen):
                        dp[y][i] = 0
                elif x > 0 and y > 0:
                    dp[y][x] = dp[y][x-1]+dp[y-1][x]
        return dp[ylen-1][xlen-1]
