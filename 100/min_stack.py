"""
source: https://leetcode.com/problems/min-stack/
author: Ramsay Leung
date: 2020-03-22
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
import bisect

# time complxity: O(n), n is the number of elements put into stack.
# space complxity: O(n), n is the number of elements put into stack.
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.descOrder = []
        self.stack = []

    def push(self, x: int) -> None:
        bisect.insort(self.descOrder, x)
        self.stack.append(x)

    def pop(self) -> None:
        removed = self.stack.pop()
        self.descOrder.remove(removed)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.descOrder[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
