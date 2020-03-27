"""
source: https://leetcode.com/problems/valid-parenthesis-string/
author: Ramsay Leung
date: 2020-02-17

 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

Note:

    The string size will be in the range [1, 100].
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        chars = list(s)
        leftBalanced = 0
        for c in chars:
            if c == '*' or c == '(':
                leftBalanced += 1
            else:
                leftBalanced -= 1
            # ensure `(` go before `)`
            if leftBalanced < 0:
                return False
        if leftBalanced == 0:
            return True
        rightBalanced = 0
        for c in reversed(chars):
            if c == ')' or c == '*':
                rightBalanced += 1
            else:
                rightBalanced -= 1
            # ensure ')' go after '('
            if rightBalanced < 0:
                return False
        return True