"""
source: https://leetcode.com/problems/binary-tree-preorder-traversal/
author: Ramsay Leung
date: 2020-03-21
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solve this problem with iterative style solution


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while len(stack) > 0 or root:
            while root:
                stack.append(root)
                root = root.left
            if stack[-1].right:
                if len(result) > 0 and stack[-1].right.val == result[-1]:
                    result.append(stack.pop().val)
                else:
                    root = stack[-1].right
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
