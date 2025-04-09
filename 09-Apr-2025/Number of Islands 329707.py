# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs (grid, row , col):
          
            if (row, col) in visited or not inbound(row, col) or grid[row][col] != "1":
                return
            visited.add((row, col))
            for r, c in directions:
                nr = row + r
                nc = col + c
                dfs(grid, nr, nc)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(grid, row, col)
                    count+=1
        return count
            

        