"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""

# dp[i][j] = palindromic[i,j]
# if s[i] == s[j]
# if i==j then dp[j][j]=True
# if i+1=j then dp[i][j]=True
# if j - i > 1 and dp[i-1][j+1] then dp[i][j]=True

# time complxity: O(n^2), n is the length of `s`
# space complxity: O(n^2), n is the length of `s`


class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        dp = [[False for x in range(slen)] for x in range(slen)]
        left = right = 0
        for j in range(slen):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j-i > 1:
                        dp[i][j] = (i+1 < slen and j-1 >= 0 and dp[i+1][j-1])
                    else:
                        dp[i][j] = True
                    if dp[i][j] and j-i+1 > right - left + 1:
                        left = i
                        right = j
        return s[left: right+1]
