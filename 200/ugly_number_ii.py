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
class Solution:
    # @profile
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        # convert to dict to improve search performance. List search is O(n),
        # dict search is O(1)
        search = {1: 0}
        i = 1
        counter = 1
        for i in dp:
            if i*2 not in search:
                bisect.insort(dp, i * 2)
                search[i*2] = 0
            if i*3 not in search:
                bisect.insort(dp, i * 3)
                search[i*3] = 0
            if i*5 not in search:
                bisect.insort(dp, i * 5)
                search[i*5] = 0
            counter += 1
            if counter >= n:
                return dp[n-1]
