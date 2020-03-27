'''
source: https://leetcode.com/problems/maximum-length-of-pair-chain/
author: Ramsay Leung
date: 2020-03-08
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:

    The number of given pairs will be in the range [1, 1000].
'''

from typing import List


# time complexity: O(NlogN), caused by sorting, and the rest of the solution is linear.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        need = -0xffffffffffff
        printAssist = []
        result = 0
        # sort by second value, beacuse second value is the cap.
        sortedPairs = sorted(pairs, key=lambda x: x[1])
        for first, second in sortedPairs:
            if first > need:
                need = second
                result += 1
        return result