"""
source: https://leetcode.com/problems/find-k-closest-elements/
author: Ramsay Leung
date: 2020-03-03

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:

    The value k is positive and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 104
    Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes. 
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        numDistanceMapping = list(tuple())
        for i, num in enumerate(arr):
            numDistanceMapping.append((num, num - x))
        # sort by value
        sortedByAbsValue = [
            mapping[0] for mapping in sorted(numDistanceMapping,
                                             key=lambda item: abs(item[1]))
        ]
        return sorted(sortedByAbsValue[:k])