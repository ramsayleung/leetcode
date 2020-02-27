"""
source: https://leetcode.com/problems/maximum-swap/
author: Ramsay Leung
date: 2020-02-27
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Note:

    The given number is in the range [0, 10e8]
"""


class Solution(object):
    def maximumSwap(self, num):
        data = list(str(num))
        value_index_map = {}
        for i, x in enumerate(data):
            value_index_map[x] = i
        for i, x in enumerate(data):
            # x will only exchange with value whch is a part of data and is greater than x
            for d in range(9, int(x), -1):
                if value_index_map.get(str(d), -1) > i:
                    data[i], data[value_index_map[str(d)]] = data[
                        value_index_map[str(d)]], data[i]
                    return int("".join(data))
        return num
