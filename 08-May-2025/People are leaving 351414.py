# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

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
    n, m = invr()
    parent = [i for i in range(n+2)]
    # size = [[i] for i in range(n+1)]


    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        r1 = find(x)
        r2= find(y)
        if r1 != r2:
            parent[r1] = parent[r2]
    
    for _ in range(m):
        s = insr()
        if s[0] == "-":
        
            union(int(s[1]), int(s[1])+1)
        else:
            x = find(int(s[1]))
            print(x if x <= n else -1)
            # print(parent)





def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()