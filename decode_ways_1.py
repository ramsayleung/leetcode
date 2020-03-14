'''
source: https://leetcode.com/problems/decode-ways/
author: Ramsay Leung
date: 2020-03-14

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


# time complexity: O(N), N is the length of `s`
# space complexity: O(N), N is the length of `s`
class Solution:
    def numDecodings(self, s: str) -> int:
        sLen = len(s)
        s = '#' + s
        dp = [0] * (sLen + 1)
        dp[0] = 1
        dp[1] = (0 if s[1] == '0' else 1)
        for i in range(2, sLen + 1):
            if s[i] == '0' and s[i - 1] >= '3':
                return 0
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] != '0' and int(f"{s[i-1]}{s[i]}") <= 26:
                dp[i] += dp[i - 2]

        return dp[sLen]
