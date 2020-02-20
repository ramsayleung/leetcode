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
from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        chars = list(s)
        # the left/right- parentiesis is high priority
        self.handleMatchParenthesis(chars, lambda c: c == '(',
                                    lambda c: c == ')', True)
        chars = list(filter(None, chars))
        print("before:", chars)
        length = len(chars)
        for i in range(length):
            if chars[i] == '(':
                for c in range(length - i):
                    if chars[c + i] == ')' or chars[c + i] == '*':
                        chars[i] = ''
                        chars[c + i] = ''
                        break
            if chars[i] == ')':
                for c in range(i + 1):
                    if chars[i - c] == '(' or chars[i - c] == '*':
                        chars[i] = ''
                        chars[i - c] = ''
                        break

        print("after: ", chars)
        return all([x == '*' or x == '' for x in chars])

    def handleMatchParenthesis(self,
                               chars: List[str],
                               leftParenthesisFunc,
                               rightParenthesisFunc,
                               firstRound=False):
        length = len(chars)
        for k in range(length if firstRound else 1):
            for i in range(length):
                if leftParenthesisFunc(chars[i]):
                    for j in range(k + 1 if firstRound else length - i):
                        if j + i >= length:
                            continue
                        if rightParenthesisFunc(chars[j + i]):
                            chars[i] = ""
                            chars[j + i] = ""
                            break

    def getFirstLeftParenthesis(self, chars: List) -> int:
        for i, c in enumerate(chars):
            if c == '(':
                return i
        return -1

    def getLastRightParenthesis(self, chars: List) -> int:
        lastIndex = -1
        for i, c in enumerate(chars):
            if c == ')':
                lastIndex = i
        return lastIndex