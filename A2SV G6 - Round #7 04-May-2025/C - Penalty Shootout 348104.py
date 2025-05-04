# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
import collections
input = sys.stdin.readline
import math

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    return list(input().strip())

def is_in_bounds(grid, i, j):
   return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():
    st = input().strip()
    p1 = []
    p2 = []
    for i in range(len(st)):
        if i % 2 == 0:
            if st[i] == "?":
                p1.append("1")
                p2.append("0")
            else:
                p1.append(st[i])
                p2.append(st[i])
        elif i % 2 != 0:
            if st[i]=="?":
                p1.append("0")
                p2.append("1")
            else:
                p1.append(st[i])
                p2.append(st[i])
    # for i in range(len(st)):
    #     if i % 2 == 0:
    #         if st[i] == "?":
    #             p2.append("0")
    #         else:
    #             p2.append(st[i])
    #     elif i % 2 != 0:
    #         if st[i]=="?":
    #             p2.append("1")
    #         else:
    #             p2.append(st[i])
    def min_kicks(p):
        ps1, ps2 = 0, 0
        for i in range(10):
            if i % 2 == 0:
                ps1 += int(p[i])
            else:
                ps2 += int(p[i])
            
            rem1 = (10 - i - 1) // 2
            rem2 = math.ceil((10 - i - 1) / 2)
            
            if ps1 > ps2 + rem2 or ps2 > ps1 + rem1:
                return i + 1
        return 10 
    
    ans1 = min_kicks(p1)
    ans2 = min_kicks(p2)
    
    print(min(ans1, ans2))
        
        



    


def main():
    multi = True  # If multiple test cases, set to True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()