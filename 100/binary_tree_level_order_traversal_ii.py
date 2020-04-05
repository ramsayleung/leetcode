"""
source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
author: Ramsay Leung
date: 2020-04-05

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


# time complexity: O(n), n is the number of nodes of given binary tree.
# space complexity: O(n), n is the number of nodes of given binary tree.
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 0)]
        result = []
        buffer = []
        currentDep = 0
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
                if currentDep != dep:
                    result.append(buffer)
                    buffer = []
                    currentDep = dep
                buffer.append(node.val)
        if len(buffer) > 0:
            result.append(buffer)
        return reversed(result)
