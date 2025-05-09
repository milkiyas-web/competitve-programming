# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import sys, collections, math, random, bisect

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input().split(" "))
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():
    n,m,q = invr()
    parent = [i for i in range(n+1)]
    size = [0] * (n+1)
    for i in range(m):
        u,v = invr()
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        r1 = find(x)
        r2 = find(y) 

        if r1 != r2:
            if size[r1] < size[r2]:
                parent[r1] = parent[r2]
                size[r2] += size[r1]
            else:
                parent[r2] = parent[r1]
                size[r1]+=size[r2]
    que = []
    for i in range(q):
        qu = insr()
        que.append(qu)
    ans = []
    for i in range(len(que)-1, -1, -1):
        if que[i][0] == "ask":
            if find(int(que[i][1])) == find(int(que[i][2])):
                ans.append("YES")
            else:
                ans.append("NO")
        else:
            union(int(que[i][1]), int(que[i][2]))
    for i in range(len(ans)-1, -1, -1):
        print(ans[i])
    






def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()