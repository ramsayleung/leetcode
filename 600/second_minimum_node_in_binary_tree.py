"""
source: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
author: Ramsay Leung
date: 2020-02-27
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.values = []

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.values.clear()
        self.values.append(root.val)
        self.treeTravel(root)
        self.values = sorted(self.values)
        for i, val in enumerate(self.values):
            if val > self.values[0]:
                return val
        return -1

    def treeTravel(self, root: TreeNode):
        if root.left is not None:
            self.values.append(self.treeTravel(root.left))
        if root.right is not None:
            self.values.append(self.treeTravel(root.right))
        return root.val
