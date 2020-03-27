"""
source: https://leetcode.com/problems/closest-binary-search-tree-value-ii/
author: Ramsay Leung
date: 2020-03-24
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

# time complxity: O(n), n is the number of nodes of given tree, mostly the
# runtime is less than O(n)
# space complxity: O(n), n is the number of nodes of given tree.


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        stack = []
        current = root
        result = Counter()
        while len(stack) > 0 or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result[current.val] = abs(current.val - target)
            if len(result) > k:
                key = result.most_common()[0][0]
                del result[key]
                if current.val - target > 0 and current.val - target > result.most_common()[0][1]:
                    break
            current = current.right
        return [x[0] for x in result.most_common()]
