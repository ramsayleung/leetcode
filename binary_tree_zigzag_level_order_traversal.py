"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# time complexity: O(n), n is the number of nodes `root` contains
# space complexity: O(n), n is the number of nodes `root` contains

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        currentDep = 0
        queue = [(root, currentDep)]
        result = []
        buffer = []
        for node, dep in queue:
            if node:
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))

                # new dep
                if currentDep != dep:
                    if len(buffer) > 0:
                        result.append(buffer if currentDep %
                                      2 == 0 else reversed(buffer))
                        buffer = list()
                    currentDep = dep
                buffer.append(node.val)
        # add nodes'values for the deepest level
        if len(buffer) > 0:
            result.append(buffer if currentDep % 2 == 0 else reversed(buffer))
        return result
