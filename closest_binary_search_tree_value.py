"""
source: https://leetcode.com/problems/closest-binary-search-tree-value/
author: Ramsay Leung
date: 2020-03-23
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxsize


# time complxity: O(n), n is the number of nodes in the given tree.
# space complxity: O(1), n is the number of nodes in the given tree.
class Solution:

    def __init__(self):
        self.dis = maxsize
        self.result = 0

    def closestValue(self, root: TreeNode, target: float) -> int:
        if root:
            self.closestValue(root.left, target)
            self.closestValue(root.right, target)
            tmp = abs(target - root.val)
            if tmp < self.dis:
                self.result = root.val
                self.dis = tmp
        return self.result
