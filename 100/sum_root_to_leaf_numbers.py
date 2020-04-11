"""
source: https://leetcode.com/problems/sum-root-to-leaf-numbers/
author: Ramsay Leung
date: 2020-04-11

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


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
        self.sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        self.helper(root, 0)
        return self.sum

    def helper(self, root: TreeNode, _sum: int):
        if root:
            if not root.left and not root.right:
                self.sum += 10*_sum+root.val
            else:
                self.helper(root.left, _sum * 10 + root.val)
                self.helper(root.right, _sum*10+root.val)
