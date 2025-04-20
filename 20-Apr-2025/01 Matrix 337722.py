# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[-1] * m for _ in range(n)]
        de = deque()
        dirr = [(1,0), (0,1), (-1,0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    res[i][j] = 0
                    de.append((i,j))
        while de:
            r, c = de.popleft()
            dist = res[r][c]
            for dr, dc in dirr:
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr == n or nc==m or res[nr][nc] != -1:
                    continue
                res[nr][nc] = dist+1
                de.append((nr, nc))

        return res