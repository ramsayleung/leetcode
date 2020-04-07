"""
source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
author: Ramsay Leung
date: 2020-04-07

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time complexity: O(n), n is the number of nodes of given tree.
# space complexity: O(1)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.find_height(root)

    def find_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.find_height(root.left)
        right = self.find_height(root.right)
        return max(left, right)+1
