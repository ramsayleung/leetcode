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


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = len(s) - 1
        decoded = ""
        repeat = 0
        while i >= 0:
            if s[i] == "]":
                if s[i - 1].isalpha():
                    encoded = self.parseString(i, s)
                    i -= (len(encoded) + 1)
                    stack.append(encoded)
                else:
                    i -= 1
            elif s[i].isdigit():
                repeat = repeat * 10 + int(s[i])
                if i - 1 >= 0 and not s[i - 1].isdigit():
                    if len(stack) > 0:
                        decoded = repeat * stack.pop() + decoded
                    else:
                        decoded = repeat * decoded
                    repeat = 0
                i -= 1
            elif s[i] == "[":
                i -= 1
            else:
                decoded = s[i] + decoded
                i -= 1
        return decoded

    def parseString(self, start: int, encoded: str) -> str:
        result = ""
        start -= 1
        while encoded[start] != "[":
            result = encoded[start] + result
            start -= 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("100[leetcode]"))
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))
