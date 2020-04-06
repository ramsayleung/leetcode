"""
source: https://leetcode.com/problems/binary-tree-right-side-view/
author: Ramsay Leung
date: 2020-04-06

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


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
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = [(root, 0)]
        lastNode = None
        answer = []
        currentDep = 0
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
                if currentDep != dep:
                    currentDep = dep
                    answer.append(lastNode.val)
                lastNode = node

        if lastNode is not None:
            answer.append(lastNode.val)
        return answer
