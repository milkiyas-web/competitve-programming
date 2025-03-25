# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    return list(input().strip())
def invr():
    return map(int, input().split())

# Defaultdict for handling missing keys automatically
def dd_int():
    return collections.defaultdict(int)
def dd_list():
    return collections.defaultdict(list)
def dd_set():
    return collections.defaultdict(set)

# Linked List Implementation

def is_in_bounds(grid, i, j):
   return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():
    n, k = invr()
    arr = inlt()

    diff = [arr[i-1] - arr[i] for i in range(1, n)]
    diff.sort()
    ans =  arr[-1] -arr[0]
    for i in range(k-1):
        ans+= diff[i]
    print(ans)


def main():
    multi = False  # If multiple test cases, set to True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()