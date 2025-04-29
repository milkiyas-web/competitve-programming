# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ## max heap
        max_h = []
        for st in stones:
            max_h.append(-st)
        heapq.heapify(max_h)
        while len(max_h) > 1:
            first = heapq.heappop(max_h)
            second = heapq.heappop(max_h)
            if second > first:
                heapq.heappush(max_h, abs(second) - abs(first))
        return abs(max_h[0]) if max_h else 0