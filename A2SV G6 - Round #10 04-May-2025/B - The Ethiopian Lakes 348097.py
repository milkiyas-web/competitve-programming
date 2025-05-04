# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

import sys
import collections

input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def invr():
    return map(int, input().split())

# Directions for moving up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():
    n, m = invr()
    visited = [[False] * m for _ in range(n)]
    grid = [inlt() for _ in range(n)]

    max_vol = 0
    def dfs(i, j):
        stack = [(i, j)]
        vol = 0
        while stack:
            x, y = stack.pop()
            if visited[x][y] or grid[x][y] == 0:
                continue
            visited[x][y] = True
            vol += grid[x][y]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_in_bounds(grid, nx, ny) and not visited[nx][ny] and grid[nx][ny] != 0:
                    stack.append((nx, ny))

        return vol
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not visited[i][j]:
                vol = dfs(i, j)
                max_vol = max(max_vol, vol)

    print(max_vol)

def main():
    multi = True  # Set to False if only one test case
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
