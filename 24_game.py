"""
source: https://leetcode.com/problems/24-game/
author: Ramsay Leung
date: 2020-02-16

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:

Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:

Input: [1, 2, 1, 2]
Output: False

Note:

    1. The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
    2. Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
    3. You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""

import operator
import itertools

from typing import List
from fractions import Fraction

operators = []
operators.append(operator.add)
operators.append(operator.sub)
operators.append(operator.mul)
operators.append(operator.truediv)

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        nums = [Fraction(x) for x in nums]
        for result in self.judgePointX(24, nums):
            return 24 == result

    def judgePointX(self, x: int, nums: List[Fraction]) -> int:
        if len(nums) == 1:
            if nums[0] == x:
                yield nums[0]
            return
        for first, second in itertools.permutations(nums, 2):
            for op in operators:
                try:
                    middleResult = op(first, second)
                except ZeroDivisionError:
                    continue
                subNums = list(nums)
                subNums.remove(first)
                subNums.remove(second)
                subNums.append(middleResult)
                for result in self.judgePointX(x, subNums):
                    yield result 