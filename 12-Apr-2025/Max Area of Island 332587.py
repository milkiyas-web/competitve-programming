# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * (m) for _ in range(n)]
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if visited[i][j] or grid[i][j] == 0:
                return 0
            
            visited[i][j] = True
            area = grid[i][j]

            for a, b in directions:
                nr = a+i
                nc = b+j

                # if grid[nr][nc] == 1 and not visited[nr][nc]:
                area += dfs(nr, nc)
            return area
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        return max_area



        