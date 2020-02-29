"""
source: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
author: Ramsay Leung
date: 2020-02-29

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:

Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).

Example 2:

Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).

Note:

    The m and n will be in the range [1, 30000].
    The k will be in the range [1, m * n]
"""

from math import floor, sqrt

# the k-th smallest is equivalent (n*m - k) = j-th largest;
# [m][n] = m * n
# when m < n:
# (n/m) = j
# decreasing order: ([m][n] -> [m][n-1] -> [m][n-2] until [m][n-j]) -> ([m-1][n] -> [m-1][n-1] -> [m-1][n-2] -> [m-1][n-j])
# j numbers as a group
# when m > n:
# (m/n) = j
# decreasing order: ([m][n] -> [m-1][n] -> [m-2][n] -> until [m-j][n]) -> ([m-1][n-1]-> [m-2][n-1] -> [m-j][n-1])
# j numbers as a group

from math import floor


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m * n
        while (low < high):
            mid = (low + high) / 2
            if self.greaterThanK(m, n, k, mid):
                high = mid
            else:
                low = mid + 1
        return int(low)

    def greaterThanK(self, m: int, n: int, k: int, multiplyResult) -> bool:
        """
        count the number of all multiplication results which are all less than multiplyResult.
        """
        counter = 0
        for i in range(1, n + 1):
            counter += min(floor(multiplyResult / i), m)
        return counter >= k
