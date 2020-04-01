"""
source: https://leetcode.com/problems/counting-bits/
author: Ramsay Leung
date: 2020-04-01
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    1. It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    2. Space complexity should be O(n).
    3. Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
from typing import List


# time complexity: O(n), n is the length of `num`
# space complexity: O(n), n is the length of `num`
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(num + 1):
            result.append(f"{bin(i)}".count("1"))
        return result
