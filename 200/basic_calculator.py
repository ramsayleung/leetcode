"""
source: https://leetcode.com/problems/basic-calculator/
author: Ramsay Leung
date: 2020-03-22
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:

    1. You may assume that the given expression is always valid.
    2. Do not use the eval built-in library function.
"""


import operator


# time complxity: O(n), n is the length of `s`
# space complxity: O(n), n is the length of `s`
class Solution:
    def __init__(self):
        self.ops = {"+": operator.add, "-": operator.sub}

    def calculate(self, s: str) -> int:
        nstack = []
        ostack = []
        num = 0
        for i, n in enumerate(s):
            if n.isdigit():
                num = num * 10 + int(n)
                if i + 1 == len(s) or not s[i + 1].isdigit():
                    nstack.append(num)
                    num = 0
                    self._calculateInside(nstack, ostack)
            elif n == "(":
                ostack.append(n)
            elif n == ")":
                index = 0
                for j, o in enumerate(ostack):
                    # get index of the last "("
                    if o == "(":
                        index = j
                ostack.pop(index)
                self._calculateInside(nstack, ostack)
            elif n in self.ops.keys():
                ostack.append(n)
        self._calculateInside(nstack, ostack)
        return nstack.pop()

    def _calculateInside(self, nstack, ostack):
        while len(ostack) > 0 and len(nstack) >= 2 and ostack[-1] != "(":
            secondOperand = nstack.pop()
            firstOperand = nstack.pop()
            op = self.ops[ostack.pop()]
            nstack.append(op(firstOperand, secondOperand))
