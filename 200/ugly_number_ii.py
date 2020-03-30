"""
source: https://leetcode.com/problems/ugly-number-ii/
author: Ramsay Leung
date: 2020-03-30

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18k
1, 2, 3, 2*2,4,2*3,2*2*2,3*3,2*5,2*2*3,3*5,2*2*2*2,2*3*3,2*2*5,2*2*2*3, 2*2*2*2*2
Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.

"""
import bisect


# xxxxx i dp.append(i) if i/2 in dp or i/3 in dp or i/5 in dp
# time complxity: O(n), n is the length of n
# space complxity: O(n), n is the length of n
class Solution:
    # @profile
    def nthUglyNumber(self, n: int) -> int:
        dp = [1, 2, 3, 4, 5, 6, 8, 9, 10]
        if n < 9:
            return dp[n - 1]
        i = dp[len(dp) - 1] + 1
        data = []
        for i in dp:
            bisect.insort(data, i * 2)
            bisect.insort(data, i * 3)
            bisect.insort(data, i * 5)
        result = dp[len(dp) - 1]
        # convert dp to dict for search performance
        dp = {x: 0 for x in dp}
        length = len(dp)
        for i in data:
            if i > result and (i / 2 in dp or i / 3 in dp or i / 5 in dp):
                dp[i] = 0
                result = i
                length += 1
                if i * 2 not in dp:
                    bisect.insort(data, i * 2)
                if i * 3 not in dp:
                    bisect.insort(data, i * 3)
                if i * 5 not in dp:
                    bisect.insort(data, i * 5)
            if length >= n:
                return result
