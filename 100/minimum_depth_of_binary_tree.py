"""
source: https://leetcode.com/problems/minimum-depth-of-binary-tree/
author: Ramsay Leung
date: 2020-04-05

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxsize


# time complexity O(n), n is the number of nodes of given tree.
# space complexity O(n), n is the number of nodes of given tree.
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [(root, 1)]
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
                if node.left is None and node.right is None:
                    return dep
        return dep
