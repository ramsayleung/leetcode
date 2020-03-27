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
        sum = [] * ylen
        for y in range(ylen):
            buffer = []
            for x in range(len(triangle[y])):
                if y > 0:
                    if x == 0:
                        buffer.append(triangle[y][x] + sum[y-1][x])
                    elif x == len(triangle[y]) - 1:
                        buffer.append(triangle[y][x] + sum[y-1][x-1])
                    else:
                        buffer.append(min(triangle[y][x] + sum[y-1][x],
                                          triangle[y][x] + sum[y-1][x-1]))
                else:
                    buffer.append(triangle[y][x])
            sum.append(buffer)
        return min(sum[ylen-1])
