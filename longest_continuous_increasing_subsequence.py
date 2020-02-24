"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:

Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:

Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

Note: Length of the array will not exceed 10,000. 
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        currentLongestSubSequence = 1
        couter = 1
        for index, num in enumerate(nums):
            if index == 0:
                continue
            pre_index = index - 1
            if nums[index] > nums[pre_index]:
                couter += 1
            else:
                couter = 1
            if couter > currentLongestSubSequence:
                currentLongestSubSequence = couter
        return currentLongestSubSequence