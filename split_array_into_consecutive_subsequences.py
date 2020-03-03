"""
source: https://leetcode.com/problems/split-array-into-consecutive-subsequences/
author: Ramsay Leung
date: 2020-03-03
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False

"""

from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        frequence = Counter(nums)
        need = Counter()
        for num in nums:
            if frequence[num] == 0:
                continue
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
            elif frequence[num + 1] > 0 and frequence[num + 2] > 0:
                frequence[num + 1] -= 1
                frequence[num + 2] -= 1
                need[num + 3] += 1
            else:
                return False
            frequence[num] -= 1
        return True