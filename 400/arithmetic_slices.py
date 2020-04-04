"""
source: https://leetcode.com/problems/arithmetic-slices/
date: 2020-04-04
author: Ramsay Leung

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7


A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""
from typing import List


# time complexity: O(n), n is the size of `A`
# space complexity: O(n), n is the size of `A`
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        size = len(A)
        dp = [0] * size
        result = 0
        for q in range(size):
            if q - 2 >= 0:
                if A[q] - A[q - 1] == A[q - 1] - A[q - 2]:
                    dp[q] = dp[q - 1] + 1
                    result += dp[q]
        return result