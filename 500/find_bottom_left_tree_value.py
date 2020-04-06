"""
source: https://leetcode.com/problems/find-bottom-left-tree-value/
author: Ramsay Leung
date: 2020-04-06

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time complexity O(n), n is the number of nodes of given tree.
# space complexity O(n), n is the number of nodes of given tree.
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [(root, 0)]
        currentDep = 0
        result = root.val
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
                if currentDep != dep:
                    currentDep = dep
                    result = node.val
        return result
