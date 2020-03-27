"""
source: https://leetcode.com/problems/bulb-switcher-ii/
author: Ramsay Leung
date: 2020-02-26

There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

    Flip all the lights.
    Flip lights with even numbers.
    Flip lights with odd numbers.
    Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

 

Example 1:

Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]

 

Example 2:

Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]

 

Example 3:

Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].

"""


class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n == 0 or m == 0:
            return 0
        # [on] [off]
        if n == 1:
            return 2
        if n == 2:
            # [off, off], [off, on], [on, off]
            if m == 1:
                return 3
            # [off, off], [off, on], [on, off], [on, on](func3 first, then func4)
            else:
                return 4
        if m == 1:
            # n >= 3
            # [off, off, off], [off, on, off], [on, off, on], [off, on, on]
            return 4
        if m == 2:
            # n >=3:
            return 7
        else:
            # m>= 3 and n >=3:
            return 8


# I use the following code to prove it n>= 3 and m >=3, the result will be 8
# from typing import List
# import itertools

# class Solution:
#     def __init__(self):
#         self.funcs = []
#         self.funcs.append(self._func1)
#         self.funcs.append(self._func2)
#         self.funcs.append(self._func3)
#         self.funcs.append(self._func4)

#     def flipLights(self, n: int, m: int) -> int:
#         if n > 3 and m > 3:
#             return 8
#         result = set()
#         bulbs = [True] * n
#         for perFunc in itertools.product(self.funcs, repeat=m):
#             input = list(bulbs)
#             for func in perFunc:
#                 func(input)
#             result.add(tuple(input))
#         for i in result:
#             print(i)
#         return len(result)

#     def _func1(self, bulbs: List[bool]) -> None:
#         for i in range(len(bulbs)):
#             bulbs[i] = not bulbs[i]

#     def _func2(self, bulbs: List[bool]) -> None:
#         for i, bulb in enumerate(bulbs):
#             if i % 2 == 0:
#                 bulbs[i] = not bulbs[i]

#     def _func3(self, bulbs: List[bool]) -> None:
#         for i, bulb in enumerate(bulbs):
#             if i % 2 == 1:
#                 bulbs[i] = not bulbs[i]

#     def _func4(self, bulbs: List[bool]) -> None:
#         kLen = int((len(bulbs) - 1) / 3)
#         for i in range(kLen + 1):
#             bulbs[i] = not bulbs[i]