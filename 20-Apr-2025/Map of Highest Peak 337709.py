# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        de = deque()
        res = [[-1] * m for _ in range(n)]
        dirr = [(0,1), (1,0), (-1,0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    de.append((i, j))
                    res[i][j] = 0
        while de:
            r, c = de.popleft()
            for dr, dc in dirr:
                nr, nc = r+dr, c+dc

                if nr < 0 or nr == n or nc < 0 or nc == m or res[nr][nc] != -1:
                    continue
                de.append((nr, nc))
                
                res[nr][nc] = res[r][c] +1

        return res

        print(de)
        