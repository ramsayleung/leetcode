"""
source: https://leetcode.com/problems/same-tree/
author: Ramsay Leung
date: 2020-04-07

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

# time complexity: O(pn+qn), pn is the number of nodes of given `p`, qn is the
# number of nodes of given `q`
# space complexity: O(pn+qn)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        plist = []
        self.inorder_traversal(p, plist)
        qlist = []
        self.inorder_traversal(q, qlist)
        return plist == qlist

    def inorder_traversal(self, root: TreeNode, order: List) -> None:
        if not root:
            return None
        order.append(self.inorder_traversal(root.left, order))
        order.append(root.val)
        order.append(self.inorder_traversal(root.right, order))
