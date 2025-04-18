# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def inbound(board, i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        
        def dfs(i,j):
            if not inbound(board, i,j) or visited[i][j] or board[i][j] != "O": 
                return
            visited[i][j] = True
            for a, b in directions:
                nr = i+a
                nc = j + b
                dfs(nr, nc)
                 
        for i in range(n):
            if board[i][0] == "O" and not visited[i][0]:
                # visited[i][0] = True
                dfs(i, 0)
            if board[i][m-1] == "O" and not visited[i][m-1]:
                # visited[i][m-1] = True
                dfs(i, m-1)
        
        for i in range(m):
            if board[0][i] == "O" and not visited[0][i]:
                # visited[0][i] = True
                dfs(0, i)
            if board[n-1][i] == "O" and not visited[n-1][i]:
                # visited[n-1][i] = True
                dfs(n-1, i)
        

        print(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and not visited[i][j]:
                    # dfs(i, j)
                    board[i][j] = "X"

        