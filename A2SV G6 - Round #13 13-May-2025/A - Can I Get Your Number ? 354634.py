# Problem: A - Can I Get Your Number ? - https://codeforces.com/gym/607625/problem/A

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
    arr = []
    ans = []
    
    for _ in range(n):
        pn = input()
        arr.append(pn)
    count = 0
    # for i in range(len(arr[0])):
    #     char = arr[0][i]
    #     all_t = True
    #     for j in range(1, n):
    #         if arr[j][i] !=  char:
    #             all_t = False
    #     if all_t:
    #         count+=1
    #     else:
    #         break
    for i in range(len(arr[0])):
        for j in range(1, n):
            if arr[j][i] != arr[0][i]:
                print(i)
                return
    # print(count)




    
    # print(ans)
        


def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()