'''
source: https://leetcode.com/problems/average-of-levels-in-binary-tree/
author: Ramsay Leung
date: 2020-03-15
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

    1. The range of node's value is in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time complexity: O(N), N is the number of nodes in the given tree.
# time complexity: O(N), N is the number of nodes in the given tree.
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        counter = _sum = currentDep = 0
        bfs = [(root, 0)]
        averages = [root.val]
        for node, dep in bfs:
            if node:
                bfs.append((node.left, dep + 1))
                bfs.append((node.right, dep + 1))
                if currentDep != dep:
                    currentDep = dep
                    averages.append(_sum / counter)
                    _sum = node.val
                    counter = 1
                else:
                    _sum += node.val
                    counter += 1
        return averages