"""
source: https://leetcode.com/problems/path-sum/
author: Ramsay Leung
date: 2020-04-10

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(root, sum, 0)

    def helper(self, root: TreeNode, target: int, sum: int) -> bool:
        if root:
            if not root.left and not root.right:
                return root.val + sum == target
            else:
                return self.helper(root.left, target, sum+root.val) or self.helper(root.right, target, sum+root.val)
        else:
            return False
