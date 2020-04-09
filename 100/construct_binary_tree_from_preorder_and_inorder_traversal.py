"""
source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
author: Ramsay Leung
date: 2020-04-09
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

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

# time complexity: O(n), n is the number of `inorder`
# space complexity: O(n), n is the number of nodes of constructed tree.

from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, 0, inorder, 0, len(inorder)-1)

    def helper(self, preorder: List[int], preStart: int, inorder: List[int], inStart: int, inend: int) -> TreeNode:
        if inStart > inend:
            return
        if inStart == inend:
            return TreeNode(inorder[inStart])
        rootNode = preorder[preStart]
        rootIndex = inorder.index(rootNode)
        leftSubtreeCount = rootIndex - inStart
        newNode = TreeNode(rootNode)
        newNode.left = self.helper(
            preorder, preStart+1, inorder, inStart, rootIndex-1)
        newNode.right = self.helper(
            preorder, preStart+leftSubtreeCount+1, inorder, rootIndex+1, inend)
        return newNode
