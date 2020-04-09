"""
source: https://leetcode.com/problems/balanced-binary-tree/
author: Ramsay Leung
date: 2020-04-09

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time complexity: O(n*logn), n is the number of nodes of given tree, logn is
# the time to findHeight.
# space complexity: O(1)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.findHeight(root.left) - self.findHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def findHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.findHeight(root.left)
        right = self.findHeight(root.height)
        return max(left, right)+1
