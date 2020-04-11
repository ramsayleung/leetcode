"""
source: https://leetcode.com/problems/binary-tree-paths/
author: Ramsay Leung
date: 2020-04-11

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


# time complexity: O(n), n is the number of nodes of given tree.
# space complexity: O(n), n is the number of nodes of given tree.
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.helper(root, "", paths)
        return paths

    def helper(self, root: TreeNode, path: str, paths: List[str]) -> None:
        if root:
            path = str(root.val) if path == "" else path + "->"+str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                self.helper(root.left, path, paths)
                self.helper(root.right, path, paths)
