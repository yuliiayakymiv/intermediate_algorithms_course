from typing import List

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        cycle = [False] * n

        # Build graph with reversed logic
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        def dfs(course):
            # Cycle detected
            if cycle[course]:
                return False
            # No prerequisite for this course
            if not graph[course]:
                return True

            cycle[course] = True
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            # Reset for other paths
            cycle[course] = False
            # Clear prerequisites since it can be completed
            graph[course] = []

            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True
