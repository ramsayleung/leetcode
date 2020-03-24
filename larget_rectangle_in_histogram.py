"""
source: https://leetcode.com/problems/largest-rectangle-in-histogram/
author: Ramsay Leung
date: 2020-03-24
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

https://assets.leetcode.com/uploads/2018/10/12/histogram.png

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png

The largest rectangle is shown in the shaded area, which has area = 10 unit.


Example:

Input: [2,1,5,6,2,3]
Output: 10


"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        result = 0
        lenOfHeights = len(heights)
        i = 0
        while i < lenOfHeights:
            if len(stack) == 0 or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                current = stack.pop()
                result = max(
                    result, heights[current] * (i if len(stack) == 0 else i - stack[-1] - 1))
                i -= 1
            i += 1
        return result


if __name__ == "__main__":
    s = Solution()

    print(s.largestRectangleArea([2, 1, 2]))
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([1, 1]))
    print(s.largestRectangleArea([1]))
    print(s.largestRectangleArea([0]))
    print(s.largestRectangleArea([]))
