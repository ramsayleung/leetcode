"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].

"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# time complxity: O(n), n is the number of all integers
# space complxity: O(n), n is the number of all integers
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self.counter = 0
        for i in nestedList:
            self.traversal(i)

    def traversal(self, nested: NestedInteger):
        if len(nested.getList()) == 0 and nested.getInteger() is not None:
            self.data.append(nested.getInteger())
        else:
            for i in nested.getList():
                self.traversal(i)

    def next(self) -> int:
        result = self.data[self.counter]
        self.counter += 1
        return result

    def hasNext(self) -> bool:
        return len(self.data) >= (self.counter+1)
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
