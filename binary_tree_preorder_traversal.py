"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.order = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.travel(root)
        return list(filter(None, self.order))

    def travel(self, root: TreeNode):
        if not root:
            return None
        self.order.append(root.val)
        self.order.append(self.travel(root.left))
        self.order.append(self.travel(root.right))
