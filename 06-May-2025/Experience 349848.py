# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
    n, m  = invr()
    parent = [i for i in range(n+1)]
    size = [1] * (n+1)
    xp = [0] * (n+1)

    def find(x):
        ans = 0
        while parent[x] != x:
            ans += xp[x]
            x = parent[x]
        return (parent[x], ans + xp[x])
    def union(x, y):
        r1, _ = find(x)
        r2, _ = find(y)

        if r1 != r2:
            if size[r1] < size[r2]:
                size[r2] +=size[r1]
                parent[r1] = parent[r2]
                xp[r1] -= xp[r2]
            else:
                size[r1] += size[r2]
                parent[r2] = parent[r1]
                xp[r2] -= xp[r1]

    for _ in range(m):
        s = insr()
        if s[0] == "add":
            par, _ = find(int(s[1]))
            xp[par]+=int(s[2])

        elif s[0] == "join":
            union(int(s[1]), int(s[2]))
        elif s[0] == "get":
            _, an = find(int(s[1]))
            print(an)


def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()