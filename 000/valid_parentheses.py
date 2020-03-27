"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

"""


# time complexity: O(n), n is the length of `s`
# space complexity: O(n), n is the length of `s`
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")":
                if len(stack) <= 0 or stack.pop() != "(":
                    return False
            elif i == "}":
                if len(stack) <= 0 or stack.pop() != "{":
                    return False
            elif i == "]":
                if len(stack) <= 0 or stack.pop() != "[":
                    return False
        return len(stack) == 0