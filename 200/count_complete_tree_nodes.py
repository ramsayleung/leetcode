"""
source: https://leetcode.com/problems/count-complete-tree-nodes/
author: Ramsay Leung
date: 2020-03-23
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time complexity : O(n), n is the number of nodes
# space complexity : O(d)=O(log⁡n), d is the tree depth, to keep the recursion stack


class Solution:
    def __init__(self):
        self.counter = 0

    def countNodes(self, root: TreeNode) -> int:
        if root:
            self.counter += 1
            self.countNodes(root.left)
            self.countNodes(root.right)
        return self.counter
