# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

import sys
import collections
from collections import deque
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

def is_in_bounds(grid, i, j):
   return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():
    n = inp()
    arr = inlt()
    de = deque()
    # print(arr)

    for i in range(n):
        if de:
            if de[-1] > arr[i] and arr[i] < de[0]:
                de.appendleft(arr[i])
            elif de[-1] > arr[i]:
                de.append(arr[i])
            elif de[-1] < arr[i]:
                de.append(arr[i])
        else:
            de.append(arr[i])
    print(*de)


def main():
    multi = True  # If multiple test cases, set to True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()