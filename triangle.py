"""
source: https://leetcode.com/problems/triangle/
author: Ramsay Leung
date: 2020-03-26
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""
# level i
# dp[i] = dp[i-1]+min(adjacent number of last row in i level)

from typing import List


# time complxity: O(n), n is the total number of all elements in the triangle
# space complxity: O(n), n is the total number of all elements in the triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ylen = len(triangle)
        xlen = len(triangle[ylen-1]) if ylen > 0 else 0
        sum = [[0 for i in range(xlen)]for i in range(ylen)]
        for y in range(ylen):
            for x in range(len(triangle[y])):
                if y > 0:
                    if x == 0:
                        sum[y][x] = triangle[y][x] + sum[y-1][x]
                    elif x == len(triangle[y]) - 1:
                        sum[y][x] = triangle[y][x] + sum[y-1][x-1]
                    else:
                        sum[y][x] = min(triangle[y][x] + sum[y-1][x],
                                        triangle[y][x] + sum[y-1][x-1])
                else:
                    sum[y][x] = triangle[y][x]
        return min(sum[ylen-1])
