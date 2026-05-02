from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacificReachable = [[False for _ in range(n)] for _ in range(m)]
        atlanticReachable = [[False for _ in range(n)] for _ in range(m)]

        def dfs(row, col, reachable):
            reachable[row][col] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if (0 <= newRow < m and 0 <= newCol < n and
                    not reachable[newRow][newCol] and
                    heights[newRow][newCol] >= heights[row][col]):
                    dfs(newRow, newCol, reachable)

        for i in range(m):
            dfs(i, 0, pacificReachable)
            dfs(i, n - 1, atlanticReachable)

        for j in range(n):
            dfs(0, j, pacificReachable)
            dfs(m - 1, j, atlanticReachable)

        result = []
        for i in range(m):
            for j in range(n):
                if pacificReachable[i][j] and atlanticReachable[i][j]:
                    result.append([i, j])

        return result
