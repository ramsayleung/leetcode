"""
source: https://leetcode.com/problems/validate-binary-search-tree/
author: Ramsay Leung
date: 2020-04-07

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    1. The left subtree of a node contains only nodes with keys less than the node's key.
    2. The right subtree of a node contains only nodes with keys greater than the node's key.
    3. Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time complexity: O(n), n is the number of nodes of given tree.
# space complexity: O(n), n is the number of nodes of given tree.
class Solution:
    def __init__(self):
        self.order = []

    def isValidBST(self, root: TreeNode) -> bool:
        self.inorder_traversal(root)
        for i in range(1, len(self.order)):
            if self.order[i] <= self.order[i-1]:
                return False
        return True

    def inorder_traversal(self, root: TreeNode) -> bool:
        if not root:
            return None
        left = self.inorder_traversal(root.left)
        if left:
            self.order.append(left)
        self.order.append(root.val)
        right = self.inorder_traversal(root.right)
        if right:
            self.order.append(right)
