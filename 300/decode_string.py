"""
source: https://leetcode.com/problems/decode-string/
author: Ramsay Leung
date: 2020-03-19

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

# time complexity: O(n), n is the length of `s`
# space complexity: O(n), n is the length of `s`


class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        wordStack = []
        repeat = 0
        word = ""
        for c in s:
            if c.isdigit():
                repeat = repeat * 10 + int(c)
            elif c == "[":
                numStack.append(repeat)
                repeat = 0
                wordStack.append(word)
                word = ""
            elif c == "]":
                wordStack[-1] += (word * numStack.pop())
                word = wordStack.pop()
            else:
                word += c
        return word if len(wordStack) == 0 else wordStack.pop()