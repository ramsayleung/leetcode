"""
source: https://leetcode.com/problems/unique-paths/
author: Ramsay Leung
date: 2020-03-26

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

"""
# dp[x][y] = dp[x-1][y] + dp[x][y-1]
# dp[x][0] = 1 dp[0][y] = 1

# time complxity: O(m*n)
# space complxity: O(m*n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for x in range(m)] for x in range(n)]
        for x in range(n):
            dp[x][0] = 1
            for y in range(m):
                dp[0][y] = 1
                if x > 0 and y > 0:
                    dp[x][y] = dp[x-1][y]+dp[x][y-1]
        return dp[n-1][m-1]
