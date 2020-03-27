'''
source: https://leetcode.com/problems/132-pattern/
author: Ramsay Leung
date: 2020-03-18
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

from sys import maxsize
from typing import List


# time complexity: O(n), n is the length of nums
# space complexity: O(n), n is the length of nums
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = -maxsize+1
        stack = []
        for num in reversed(nums):
            if num < third:
                return True
            while(len(stack) > 0 and num > stack[-1]):
                third = stack[-1]
                stack.pop()
            stack.append(num)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.find132pattern([8, 10, 4, 6, 5]))
    print(s.find132pattern([-2, 1, 2, -2, 1, 2]))
    print(s.find132pattern([1, 2, 3, 4]))
    print(s.find132pattern([3, 5, 0, 3, 4]))
    print(s.find132pattern([-1, 3, 2, 0]))
    print(s.find132pattern([3, 1, 4, 2]))
