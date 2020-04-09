"""
source: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
author: Ramsay Leung
date: 2020-04-09

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time complexity: O(n), n is the number of `inorder`.
# space complexity: O(n), n is the space which needs to contruct a tree.
from typing import Dict, List


class Solution:
    def __init__(self):
        self.inorderDict: Dict[int, int] = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorderDict = {
            value: index
            for index, value in enumerate(inorder)
        }
        return self.helper(postorder,
                           len(postorder) - 1, inorder, 0,
                           len(inorder) - 1)

    def helper(self, postorder: List[int], postEnd: int, inorder: List[int],
               inStart: int, inEnd: int) -> TreeNode:
        if inStart > inEnd:
            return None
        elif inStart == inEnd:
            return TreeNode(inorder[inStart])
        root = postorder[postEnd]
        rootIndex = self.inorderDict[root]
        rightSubtreeCount = inEnd - rootIndex
        newNode = TreeNode(root)
        newNode.left = self.helper(postorder, postEnd - rightSubtreeCount - 1,
                                   inorder, inStart, rootIndex - 1)
        newNode.right = self.helper(postorder, postEnd - 1, inorder,
                                    rootIndex + 1, inEnd)
        return newNode
