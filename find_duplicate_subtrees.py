'''
source: https://leetcode.com/problems/find-duplicate-subtrees/
author: Ramsay Leung
date: 2020-03-06
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from collections import Counter


class Solution:
    def __init__(self):
        self.count = Counter()
        self.result = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.serial(root)
        return self.result

    def serial(self, root: TreeNode):
        if not root:
            return " "
        id = f"{root.val}_{self.serial(root.left)}_{self.serial(root.right)}"
        self.count[id] += 1
        if self.count[id] == 2:
            self.result.append(root)
        return id
