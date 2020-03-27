"""
source: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
author: Ramsay Leung
date: 2020-03-23
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:

Input: "1,#"
Output: false

Example 3:

Input: "9,#,#,1"
Output: false
"""

# time complxity: O(n), n is the length of `preorder`
# space complxity: O(1)


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        correntCounter = 0
        deserialize = preorder.split(",")
        for node in deserialize[: len(deserialize)-1]:
            if node.isdigit():
                correntCounter += 1
            elif node == "#":
                correntCounter -= 1
            if correntCounter < 0:
                return False
        return correntCounter == 0 and deserialize[-1] == "#"
