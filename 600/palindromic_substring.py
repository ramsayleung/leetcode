'''
source: https://leetcode.com/problems/palindromic-substrings/
author: Ramsay Leung
date: 2020-03-08
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

# time complexity: O(N**2), N is the length of `s`
# space complexity: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        strLen = len(s)
        result = 0
        for i in range(strLen):
            # when len of palidrome is odd, i means the middle number
            result += self.countPalindromic(s, i, i)
            # when len of palidrome is event, i means the middle left number, i+1 means the middle right number
            result += self.countPalindromic(s, i, i + 1)
        return result

    def countPalindromic(self, s: str, left: int, right: int) -> int:
        result = 0
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            result += 1
        return result