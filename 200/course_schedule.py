"""
source: https://leetcode.com/problems/course-schedule/
author: Ramsay Leung
date: 2020-04-06

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    + The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    + You may assume that there are no duplicate edges in the input prerequisites.
    + 1 <= numCourses <= 10^5
"""
from collections import defaultdict
from typing import List


# time complexity: O(V+N), V is the number of vertices, N is the number of nodes.
# space complexity: O(V), V is the number of vertices
class Graph:
    def __init__(self, numCourse: int, vertices: List[List[int]]):
        self.adjacency = defaultdict(list)
        for first, second in vertices:
            self.adjacency[first].append(second)
        # number of vertices
        self.number = numCourse

    def dfs(self, vertice: int, visited: List[bool], recursion: List[bool]) -> bool:
        if not visited[vertice]:
            # mark this vertice visited.
            visited[vertice] = True
            recursion[vertice] = True
            nodes = self.adjacency[vertice]
            for node in nodes:
                if not visited[node] and self.dfs(node, visited, recursion):
                    return True
                elif recursion[node]:
                    return True
        recursion[vertice] = False
        return False

    def isCycle(self) -> bool:
        visited = [False] * self.number
        recursion = [False] * self.number
        for v in range(self.number):
            if self.dfs(v, visited, recursion):
                return True
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = Graph(numCourses, prerequisites)
        return not graph.isCycle()
