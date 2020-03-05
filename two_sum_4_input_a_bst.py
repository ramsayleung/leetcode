'''
source: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
author: Ramsay
date: 2020-03-05
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.data = []

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.data.append(root.val)
        self.travelTree(root)
        for i, d in enumerate(self.data):
            if (k - d) in self.data and seld.data.index(d) != self.data.index(
                    k - d):
                return True
        return False

    def travelTree(self, root: TreeNode):
        if root.left:
            self.data.append(self.travelTree(root.left))
        if root.right:
            self.data.append(self.travelTree(root.right))
        return root.val