"""
source: https://leetcode.com/problems/range-sum-query-immutable/
author: Ramsay Leung
date: 2020-03-31

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.

"""
from typing import List


# time complxity: O(n), n is the size of nums
# space complxity: O(n), n is the size of nums
class NumArray:
    def __init__(self, nums: List[int]):
        self.data = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.data[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
