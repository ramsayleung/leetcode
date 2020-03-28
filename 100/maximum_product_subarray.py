"""
source: https://leetcode.com/problems/maximum-product-subarray/
author: Ramsay Leung
date: 2020-03-28

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
from sys import maxsize
from typing import List


# time complexity: O(n), n is the number of nums
# space complexity: O(n), n is the number of nums
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        maxDp = [1] * size
        minDp = [1] * size
        maxProduct = maxDp[0] = minDp[0] = nums[0]
        for i in range(1, size):
            _maxtmp = maxDp[i-1]*nums[i]
            _mintmp = minDp[i-1]*nums[i]
            maxDp[i] = max(_maxtmp, _mintmp, nums[i])
            minDp[i] = min(_maxtmp, _mintmp, nums[i])
            maxProduct = max(maxProduct, maxDp[i])
        return maxProduct
