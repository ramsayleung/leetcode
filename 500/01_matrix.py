"""
source: https://leetcode.com/problems/01-matrix/
author: Ramsay Leung
date: 2020-04-07

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

    1. The number of elements of the given matrix will not exceed 10,000.
    2. There are at least one 0 in the given matrix.
    3. The cells are adjacent in only four directions: up, down, left and right.
"""

from sys import maxsize
from typing import List

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# time complexity: O(r*c), r is the number of row, c is the number of col.
# space complexity: O(r*c), r is the number of row, c is the number of col.


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        direction = [DOWN, UP, LEFT, RIGHT]
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        queue = []
        distance = [[maxsize for i in range(cols)]for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    distance[row][col] = 0
                    queue.append((row, col))
        for row, col in queue:
            for d in direction:
                new_row = row+d[0]
                new_col = col+d[1]
                if new_row >= 0 and new_col >= 0 and new_row < rows and new_col < cols:
                    if distance[new_row][new_col] > distance[row][col]+1:
                        distance[new_row][new_col] = distance[row][col]+1
                        queue.append((new_row, new_col))
        return distance
