"""
source: https://leetcode.com/problems/is-subsequence/
author: Ramsay Leung
date: 2020-04-04

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""


# time complxity: O(n), n is the size of `t`
# space complxity: O(n), n is smaller than the size of `t`
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # to improve search performance.
        search = set(t)
        _index = 0
        for c in s:
            if c in search:
                try:
                    _index = t.index(c, _index) if _index == 0 else t.index(
                        c, _index + 1)
                except ValueError:
                    return False
            else:
                return False
        return True