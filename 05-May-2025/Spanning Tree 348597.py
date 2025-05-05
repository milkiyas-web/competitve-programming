# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
    n, m = invr()
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    # vals = []
    arr = []
    
    # vals = dict()
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_ = find(x)
        y_ = find(y) 

        if x_ == y_:
            return False
        if rank[x_] > rank[y_]:
                parent[y_] = x_
                rank[x_] += rank[y_]
        else:
            parent[x_] = y_
            rank[y_]+=rank[x_]
        return True
    for i in range(m):
        b,e,w = invr()
        # vals.append((w,b,e)) 
        # union(b,e,w)
        # vals[w] = (b,e)
        arr.append([b,e,w])
    arr.sort(key = lambda x: x[2])
    ans = 0
    for i in range(len(arr)):
        
        # print(ans)
        if union(arr[i][0], arr[i][1]):
            ans+=arr[i][2]
    print(ans)
    

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()