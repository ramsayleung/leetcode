"""
source: https://leetcode.com/problems/binary-tree-inorder-traversal/
author: Ramsay Leung
date: 2020-03-21
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# time complexity: O(n), n is the number of nodes `root` contains
# space complexity: O(n), n is the number of nodes `root` contains
class Solution:
    def __init__(self):
        self.order = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.travel(root)
        filter(None, self.order)
        return self.order

    def travel(self, root: TreeNode):
        if not root:
            return None
        self.order.append(self.travel(root.left))
        self.order.append(root.val)
        self.order.append(self.travel(root.right))
