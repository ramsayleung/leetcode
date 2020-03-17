"""
source: https://leetcode.com/problems/next-greater-element-i/
author: Ramsay Leung
date: 2020-03-17
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:

    1. All elements in nums1 and nums2 are unique.
    2. The length of both nums1 and nums2 would not exceed 1000.
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lenNums1 = len(nums1)
        ans = [-1] * lenNums1
        for i, num in enumerate(nums1):
            index = nums2.index(num)
            for j in range(index, len(nums2)):
                if nums2[j] > num:
                    ans[i] = nums2[j]
                    break
        return ans
