"""
source: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
author: Ramsay Leung
date: 2020-04-06

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:

    1. The height of the n-ary tree is less than or equal to 1000
    2. The total number of nodes is between [0, 10^4]

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# time complexity: O(n), n is the number of nodes of given n-ary tree
# space complexity: O(n), n is the number of nodes of given n-ary tree


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [(root, 0)]
        currentDep = 0
        buffer = []
        result = []
        for node, dep in queue:
            if node:
                for child in node.children:
                    queue.append((child, dep+1))
                if currentDep != dep:
                    currentDep = dep
                    result.append(buffer)
                    buffer = []
                buffer.append(node.val)
        if len(buffer) > 0:
            result.append(buffer)
        return result
