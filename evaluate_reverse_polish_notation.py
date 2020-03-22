"""
source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
author: Ramsay Leung
date: 2020-03-22

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
import operator
from typing import List


# time complxity: O(n), n is the length of `token`
# space complxity: O(n), n is the length of `token`
class Solution:
    def __init__(self):
        self.operators = {"+": operator.add, "-": operator.sub,
                          "*": operator.mul, "/": operator.truediv}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.operators.keys():
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                if token == "/":
                    # truncate toward zero
                    tmp = int(self.operators[token](
                        float(firstOperand), secondOperand))
                else:
                    tmp = self.operators[token](firstOperand, secondOperand)
                stack.append(tmp)
            else:
                stack.append(int(token))
        return stack.pop()
