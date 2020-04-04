"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""
from typing import List


# time complexity: O(n**2), n is the size of nums
# space complexity: O(n), n is the size of nums
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        partition = int(_sum / 2)
        size = len(nums)
        nums = sorted(nums)
        dp = [False] * (partition + 1)
        dp[0] = True
        for num in nums:
            for i in range(partition, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        return dp[partition]
