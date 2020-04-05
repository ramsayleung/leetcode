"""
source: https://leetcode.com/problems/binary-tree-level-order-traversal/
author: Ramsay Leung
date: 2020-04-05

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


# time complexity O(n), n is number of nodes of the given binary tree.
# space complexity O(n), n is number of nodes of the given binary tree.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 0)]
        buffer = []
        result = []
        currentDep = 0
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
                if currentDep != dep:
                    currentDep = dep
                    result.append(buffer)
                    buffer = []
                buffer.append(node.val)
        if len(buffer) > 0:
            result.append(buffer)
        return result
