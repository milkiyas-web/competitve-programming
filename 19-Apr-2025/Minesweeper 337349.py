# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
       
        dirr = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1, -1), (-1,1)]
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        r, c = click
        if board[r][c]== "M":
            board[r][c] = "X"
            return board
        def dfs(i, j):
            if board[i][j] != "E":
                return
            count = 0
            for a, b in dirr:
                nr = i+a
                nc = j+b
                if 0<=nr<n and 0<= nc<m:
                    if board[nr][nc] == "M":
                        count+=1
            if count >0:
                board[i][j] = str(count)
                return
            board[i][j] = "B"
            for a, b in dirr:
                nr, nc = a+i, b+j
                if 0<=nr<n and 0<= nc<m:
                    dfs(nr, nc)      
        dfs(r,c)
        return board

