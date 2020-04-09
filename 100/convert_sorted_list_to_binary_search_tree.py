"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time complexity: O(n*2) = O(n), n is the length of given linked list.
# space complexity: O(n), n is the space of helper array we need to help to
# construct tree..


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        input = []
        while head:
            input.append(head.val)
            head = head.next
        return self.helper(input)

    def helper(self, input: List[int]) -> TreeNode:
        if len(input) == 1:
            return TreeNode(input[0])
        if len(input) > 1:
            index = len(input)//2
            root = TreeNode(input[index])
            root.left = self.helper(input[:index])
            root.right = self.helper(input[index+1:])
            return root
