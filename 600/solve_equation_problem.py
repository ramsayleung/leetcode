"""
source: https://leetcode.com/problems/solve-the-equation/
author: Ramsay Leung
date: 2020-03-14
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:

Input: "x=x"
Output: "Infinite solutions"

Example 3:

Input: "2x=x"
Output: "x=0"

Example 4:

Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:

Input: "x=x+2"
Output: "No solution"
"""

from typing import List


# time complexity: O(N), N is the length of `s`
# space complexity: O(N), N is the length of `s`
class Solution:
    def __init__(self):
        self.ins = "Infinite solutions"
        self.ns = "No solution"

    def solveEquation(self, equation: str) -> str:
        pos = equation.index("=")
        left = self.parse(equation[:pos])
        right = self.parse(equation[pos + 1:])
        left[0] -= right[0]
        left[1] -= right[1]
        if left[0] == 0:
            return self.ins if left[1] == 0 else self.ns
        else:
            return f"x={-int(left[1]/left[0])}"

    def parse(self, s: str) -> List:
        """
        convert expression to `ax+b`
        """
        # counts of x
        a = b = tmp = 0
        isDigit = False
        sign = 1
        for char in s:
            if char.isdigit():
                # case: 333
                tmp = tmp * 10 + int(char)
                isDigit = True
            else:
                if char == 'x':
                    # case: `70x` the digit followed by `x`, add it to `a`
                    a += (tmp if isDigit else 1) * sign
                else:
                    # case: `7 -` the digit doesn't followed by `x`, add it `b`
                    b += tmp * sign
                    sign = (1 if char == '+' else -1)
                isDigit = False
                tmp = 0
        # if the last char is digit, then tmp is a number, adds tmp to `b`
        if isDigit:
            b += tmp * sign
        return [a, b]