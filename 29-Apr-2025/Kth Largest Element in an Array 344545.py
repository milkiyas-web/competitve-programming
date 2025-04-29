# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums
        heapq.heapify(h)
        print(h)
        while len(h) > k:
            heapq.heappop(h)
        return h[0]
        