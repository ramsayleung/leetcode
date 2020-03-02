"""
source: https://leetcode.com/problems/maximum-width-of-binary-tree/
author: Ramsay Leung
date: 2020-03-02
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # (root, depth, pos)
        queue = [(root, 0, 0)]
        currentDepth = result = left = 0
        for root, depth, pos in queue:
            if root:
                queue.append((root.left, depth + 1, pos * 2))
                queue.append((root.right, depth + 1, pos * 2 + 1))
                # travel into new depth
                if currentDepth != depth:
                    currentDepth = depth
                    # when goes into a new depth, the left pos goes before right pos
                    left = pos
                result = max(result, pos - left + 1)
        return result
