'''
source: https://leetcode.com/problems/decode-ways-ii/
author: Ramsay Leung
date: 2020-03-14
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:

Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:

Input: "1*"
Output: 9 + 9 = 18

Note:

    The length of the input string will fit in range [1, 105].
    The input string will only contain the character '*' and digits '0' - '9'.
'''


# time complexity: O(30*N)->O(N), N is the length of `s`
# space complexity: O(N), N is the length of `s`
class Solution:
    def numDecodings(self, s: str) -> int:
        sLen = len(s)
        s = '#' + s
        dp = [0] * (sLen + 1)
        dp[0] = 1
        dp[1] = 9 if s[1] == '*' else 0 if s[1] == '0' else 1
        for i in range(2, sLen + 1):
            if s[i] == '*':
                for j in range(1, 10):
                    dp[i] += dp[i - 1]
                    if s[i - 1] == '*':
                        for k in range(1, 3):
                            if int(f"{k}{j}") <= 26:
                                dp[i] += dp[i - 2]
                    else:
                        if s[i - 1] != '0' and int(f"{s[i-1]}{j}") <= 26:
                            dp[i] += dp[i - 2]
            else:
                if s[i] != '0':
                    dp[i] += dp[i - 1]
                if s[i - 1] == '*':
                    for k in range(1, 3):
                        if int(f"{k}{s[i]}") <= 26:
                            dp[i] += dp[i - 2]
                else:
                    if s[i - 1] != '0' and int(f"{s[i-1]}{s[i]}") <= 26:
                        dp[i] += dp[i - 2]
        return dp[sLen] if dp[sLen] < 10**9 else dp[sLen] % (10**9 + 7)