"""
source: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
date: 2020-04-10
author: Ramsay Leung

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time complexity: O(n), n is the number of nodes of given tree.
# space complexity: O(1)


class Solution:
    def __init__(self):
        self.pre = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        print(f"root={root},pre={self.pre}")
        root.right = self.pre
        root.left = None
        self.pre = root
