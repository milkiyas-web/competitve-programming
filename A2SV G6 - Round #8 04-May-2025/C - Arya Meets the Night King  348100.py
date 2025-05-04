# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

import sys
import collections
import bisect
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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node

    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print('None')

def is_in_bounds(grid, i, j):
   return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():
    s, b = invr()
    arr = inlt()
    ans = []
    for i in range(b):
        d, g = invr()
        ans.append((d, g))
    ans.sort()
    pre = [0] * (b+1)
    for i in range(b):
        pre[i + 1] = pre[i] + ans[i][1]
    answer = []
    for power in arr:
        idx = bisect.bisect_right(ans, (power, float('inf'))) - 1
        answer.append(pre[idx + 1])
    print(*answer)
def main():
    multi = False  # If multiple test cases, set to True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()