"""
source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
author: Ramsay Leung
date: 2020-04-09

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


# time complexity: O(n), n is the number of `nums`
# space complexity: O(n), n is the space of which tree needs to contruct
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) > 1:
            index = len(nums) // 2
            root = TreeNode(nums[index])
            root.left = self.sortedArrayToBST(nums[:index])
            root.right = self.sortedArrayToBST(nums[index + 1:])
            return root
