# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

import sys, collections, math, random, bisect

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():
    n = inp()
    arr = inlt()
    graph = dd(set)
    # parent = [0] * len(arr)
    visited = [False] * (n+1)
    for i, v in enumerate(arr):
        graph[i+1].add(v)
        graph[v].add(i+1)

    count= 0
    # def bfs(v):
    #     de = collections.deque([v])
    #     visited[v] = True 
    #     while de:
    #         n = de.popleft()
    #         for ne in graph[n]:
    #             if not visited[ne]:
    #                 visited[ne] = True 
    #                 de.append(ne)
         
    # for i in range(1, n+1):
    #     if not visited[i]:
    #         bfs(i)
    #         count+=1
    # print(count)
    parent = [i for i in range(n+1)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x_ = find(x)
        y_ = find(y)

        if x_ != y_:
            parent[y_] = x_ 
    for i, v in enumerate(arr):
        union(i+1, v)
    ans = set()
    for i in range(1, n+1):
        ans.add(find(i))
    print(len(ans))




    

    
    # count= 0
    # def dfs(v):
    #     visited[v] = True 
    #     for ne in graph[v]:
    #         if not visited[ne]:
    #             # continue
    #             dfs(ne)
            

    # for i in range(1,n+1):
    #     if not visited[i]:
    #         dfs(i)
    #         count+=1
    # print(count)
def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()