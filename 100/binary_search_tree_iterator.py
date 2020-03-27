"""
source: https://leetcode.com/problems/binary-search-tree-iterator/
author: Ramsay Leung
date: 2020-03-22

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:

https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note:

    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion style
# time complxity: O(n), n is the number of nodes in the given tree.
# space complxity: O(n), n is the number of nodes in the given tree.


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = []
        self.traversal(root)
        self.counter = 0

    def traversal(self, root: TreeNode):
        stack = []
        current = root
        while len(stack) > 0 and current is not None:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            self.data.append(current.val)
            current = current.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.data[self.counter]
        self.counter += 1
        return n

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.data) >= self.counter+1

# Iteration style
# time complxity: O(n), n is the number of nodes in the given tree.
# space complxity: O(n), n is the number of nodes in the given tree.


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.current = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
        self.current = self.stack.pop()
        value = self.current.val
        self.current = self.current.right
        return value

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0 or self.current


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
