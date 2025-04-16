# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirr = [(0,1), (0,-1), (1,0), (-1, 0)]
        n = len(grid)
        m = len(grid[0])
        visited = set()
        de = deque()
        count=0
        fresh, rott = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    # rott+=1
                    de.append((i,j))
        while de and fresh > 0:
            for i in range(len(de)):
                # print(de)
                r,c = de.popleft()
                for a, b in dirr:
                    row = r + a
                    col = c + b
                    if (row < 0 or row == n or col < 0 or col == m or grid[row][col] != 1):
                        continue
                    print(grid)
                    grid[row][col] = 2
                    de.append((row,col))
                    fresh-=1
            count+=1
            # print(count)
        if fresh == 0:
            return count 
        else:
            return -1
