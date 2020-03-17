"""
source: https://leetcode.com/problems/next-greater-element-ii/
author: Ramsay Leung
date: 2020-03-17

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000. 
"""

from typing import List


# time complxity: O(2*n)->O(n), n is the length of `nums`
# space complxity: O(n), n is the length of `nums`
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        numNextGreaterElementsMap = {}

        self.traverse(stack, numNextGreaterElementsMap, nums)

        # the second time to traverse nums equals to traverse num circularly.
        self.traverse(stack, numNextGreaterElementsMap, nums)
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            if i in numNextGreaterElementsMap:
                ans[i] = numNextGreaterElementsMap[i]
        return ans

    def traverse(self, stack: List[int], numNextGreaterElementsMap, nums: List[int]) -> None:
        for i, num in enumerate(nums):
            while len(stack) > 0 and num > stack[-1][1]:
                numNextGreaterElementsMap[stack[-1][0]] = num
                stack.pop()
            stack.append((i, num))
