# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

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
    n, k = invr()
    arr = inlt()
    de = deque()
    
    ex = set()
    
    for i in arr:
        if i in ex:
            continue  

        if len(de) >= k:
            last = de.pop() 
            ex.remove(last)  

        de.appendleft(i)  
        ex.add(i)
    
    print(len(de))           
    print(*de)

def main():
    multi = False  # If multiple test cases, set to True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()