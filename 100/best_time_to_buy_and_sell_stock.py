"""
source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
author: Ramsay Leung
date: 2020-03-27
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# xxxx i dp[i] = min(dp[i-1],prices[i]) profit = prices[i] - dp[i]
# dp[i] means the lowest price between day0 -> dayi
from typing import List


# time complexity O(n), n is the number of prices
# space complexity O(n), n is the number of prices
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pricesLen = len(prices)
        dp = [0] * pricesLen
        profit = 0
        for i in range(pricesLen):
            if i == 0:
                dp[i] = prices[i]
            else:
                dp[i] = min(dp[i-1], prices[i])
                tmp = prices[i] - dp[i]
                if tmp > profit:
                    profit = tmp
        return profit
