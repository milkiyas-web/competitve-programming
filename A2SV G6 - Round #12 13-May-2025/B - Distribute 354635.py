# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

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
    sor = sorted([[arr[i], i+1] for i in range(n)])
    ans = []
    i = 0
    j = len(sor)-1
    while i < j:
        ans.append((sor[i][1], sor[j][1]))
        i+=1
        j-=1
    for a, b in ans:
        print(a, b)

    



    # for i in range()
def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()