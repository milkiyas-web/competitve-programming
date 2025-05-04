# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

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
    n = inp()
    a = inlt()
    last = 0
    for num in a:
        last+=1
        if last == num:
            last+=1
    
    print(last)
   
    
   
   
    # else:
    #     de.append(arr[n-1] +1)
    #     de.popleft()
        
    # print(de[-1])
    # if arr[0]-1 != 0:
    #     de.appendleft(arr[0]-1)
    #     de.pop()
    #     print(de[-1])
    #     return
    # else:
    #     de.append(arr[n-1] +1)
    #     de.popleft()
    #     print(de[-1])
    #     return

def main():
    multi = True  # If multiple test cases, set to True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()