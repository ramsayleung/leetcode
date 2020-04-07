"""
source: https://leetcode.com/problems/find-largest-value-in-each-tree-row//
author: Ramsay Leung
date: 2020-04-06
You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxsize

# time complexity: O(n), n is the number of nodes of given tree.
# space complexity: O(L), L is the number of level of given tree.
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = [(root, 0)]
        currentDep = 0
        largest = -maxsize + 1
        result = []
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
                if currentDep != dep:
                    result.append(largest)
                    currentDep = dep
                    largest = -maxsize + 1
                largest = max(largest, node.val)
        if largest != -maxsize + 1:
            result.append(largest)
        return result
