"""
source: https://leetcode.com/problems/symmetric-tree/
author: Ramsay Leung
date: 2020-04-05

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

 

Note:
Bonus points if you could solve it both recursively and iteratively.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


# time complexity O(n), n is the size of given binary tree.
# space complexity O(n), n is the size of given binary tree.
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [(root, 0)]
        currentDep = 0
        buffer = []
        for node, depth in queue:
            if node:
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
            if currentDep != depth:
                currentDep = depth
                if not self.checkSymmetric(buffer):
                    return False
                buffer = []
            buffer.append(node.val if node else None)
        return self.checkSymmetric(buffer)

    def checkSymmetric(self, values: List[int]) -> bool:
        length = len(values)
        if length == 0:
            return True
        for i in range(int(length/2)):
            if values[i] != values[length-i-1]:
                return False
        return True
