"""
source: https://leetcode.com/problems/target-sum/
author: Ramsay Leung
date: 2020-04-02

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3 -1->0->1->2->3
+1-1+1+1+1 = 3 1->0->1->2->3
+1+1-1+1+1 = 3 1->2->1->2->3
+1+1+1-1+1 = 3 1->2->3->2->3
+1+1+1+1-1 = 3 1->2->3-4->3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

    1. The length of the given array is positive and will not exceed 20.
    2. The sum of elements in the given array will not exceed 1000.
    3. Your output answer is guaranteed to be fitted in a 32-bit integer.

"""
from collections import Counter
from typing import List


# dp[i][j] means the count of sum equals j in subArray sums[0:i]
# time complexity: O(n**2), n is length of `nums`
# space complexity: O(n**2), n is length of `nums`
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        size = len(nums)
        dp = []
        for i in range(size + 1):
            dp.append(Counter())
        dp[0][0] = 1
        for i in range(size):
            for _sum, count in dp[i].most_common():
                dp[i + 1][_sum - nums[i]] += count
                dp[i + 1][_sum + nums[i]] += count
        return dp[size][S]
