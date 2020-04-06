"""
source: https://leetcode.com/problems/number-of-islands/
author: Ramsay Leung
date: 2020-04-06

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""
from typing import List, Tuple

# time complexity: O(h*w), h is the number of rows of grid, w is the number of
# columns of grid.
# space complexity: O(min(h,w)), because in the worst case where the grid is
# filled with lands, the size of queue can grow up to min(h,w).

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        heigth = len(grid)
        width = len(grid[0]) if heigth > 0 else 0
        number_of_island = 0
        queue = []
        for y in range(heigth):
            for x in range(width):
                if grid[y][x] == "1":
                    number_of_island += 1
                    # mark this cell as visited
                    grid[y][x] = "0"
                    queue.append((y, x))
                    self.bfs(grid, queue)
        return number_of_island

    def bfs(self, grid: List[List[str]], queue: List[Tuple[int, int]]) -> None:
        height = len(grid)
        width = len(grid[0]) if height > 0 else 0
        for row, col in queue:
            if row - 1 >= 0 and grid[row - 1][col] == "1":
                grid[row - 1][col] = "0"
                queue.append((row - 1, col))
            if row + 1 < height and grid[row + 1][col] == "1":
                grid[row + 1][col] = "0"
                queue.append((row + 1, col))
            if col - 1 >= 0 and grid[row][col - 1] == "1":
                grid[row][col - 1] = "0"
                queue.append((row, col - 1))
            if col + 1 < width and grid[row][col + 1] == "1":
                grid[row][col + 1] = "0"
                queue.append((row, col + 1))
        queue.clear()
