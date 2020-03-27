"""
source: https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3

Example 1:

Input: [5,2,6,1,3]
Output: false

Example 2:

Input: [5,2,1,3,6]
Output: true

Follow up:
Could you do it using only constant space complexity?
"""
from sys import maxsize
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if len(preorder) == 0:
            return True
        stack = []
        leftmost = - maxsize + 1
        for i in preorder:
            if i < leftmost:
                return False
            while len(stack) > 0 and i > stack[-1]:
                leftmost = stack.pop()
            stack.append(i)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.verifyPreorder([1, 3, 2, 4]))
    print(s.verifyPreorder([2, 1]))
    print(s.verifyPreorder([5, 2, 6, 1, 3]))
    print(s.verifyPreorder([5, 2, 1, 3, 6]))
    print(s.verifyPreorder([1, 3, 2]))
