"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

https://assets.leetcode.com/static_assets/public/images/courses/range_sum_query_2d.png

The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

"""
from typing import List


# time complxity: O(m*n), m is the row size of `matrix`, n is the col size of `matrix`
# space complxity: O(m*n), m is the row size of `matrix`, n is the col size of `matrix`
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.data = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sum = 0
        for y in range(row1, row2 + 1):
            for x in range(col1, col2 + 1):
                _sum += self.data[y][x]
        return _sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
