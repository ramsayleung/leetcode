"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"

Example 2:

Input: "cbacdcbc"
Output: "acdb"

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""


# time complexity: O(n), n is the length of `s`
# space complexity: O(n), n is the length of `s`
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i, num in enumerate(s):
            while len(stack) > 0 and num < stack[-1] and s.count(
                    stack[-1], i) > 0 and num not in stack:
                stack.pop()
            if num not in stack:
                stack.append(num)
        return "".join(stack)