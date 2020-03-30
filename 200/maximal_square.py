"""
source: https://leetcode.com/problems/maximal-square/
author: Ramsay Leung
date: 2020-03-30

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""
from typing import List


# dp[j][i] = min(dp[j-1][i-1],dp[j][i-1],dp[j-1][i]) +1
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        if height == 0:
            return 0
        width = len(matrix[0])
        dp = [[0 for x in range(width+1)]for x in range(height+1)]
        largestSize = 0
        for j in range(1, height+1):
            for i in range(1, width+1):
                if matrix[j-1][i-1] == "1":
                    dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1])+1
                largestSize = max(dp[j][i], largestSize)
        return largestSize ** 2
