'''
source: https://leetcode.com/problems/print-binary-tree/
author: Ramsay Leung
date: 2020-03-04
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from math import floor


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        m = self.findHeight(root)
        # n is defined by m
        n = 2**m - 1
        buffer = [["" for i in range(n)] for j in range(m)]
        middlePos = (n + 1) / 2
        nodeDepthPos = [(root, 1, middlePos)]
        for node, depth, pos in nodeDepthPos:
            if node is not None:
                nodeDepthPos.append((node.left, depth + 1,
                                     floor(pos - middlePos / (2**depth))))
                nodeDepthPos.append((node.right, depth + 1,
                                     floor(pos + middlePos / (2**depth))))
                print(f"pos={pos}, depth={depth} val={node.val}")
                buffer[depth - 1][int(pos) - 1] = str(node.val)
        return buffer

    def findHeight(self, root: TreeNode):
        if root is None:
            return 0
        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)
        return max(leftHeight, rightHeight) + 1
