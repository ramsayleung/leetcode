"""
source: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
author: Ramsay Leung
date: 2020-04-07
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Output: 5

Constraints:

    1. The depth of the n-ary tree is less than or equal to 1000.
    2. The total number of nodes is between [0, 10^4].


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# time complexity: O(n), n is the number of nodes of given tree.
# space complexity: O(n), n is the number of nodes of given tree.


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = [(root, 1)]
        maxDep = 0
        for node, dep in queue:
            if node:
                for child in node.children:
                    queue.append((child, dep+1))
                maxDep = max(maxDep, dep)
        return maxDep
