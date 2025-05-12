# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

from heapq import heappush, heappop
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        i = 0
        while i < n or min_heap:
            while i < n and tasks[i][0] <= time:
                enqueue_time, processing_time, idx = tasks[i]
                heappush(min_heap, (processing_time, idx))
                i += 1
            if min_heap:
                proc_time, idx = heappop(min_heap)
                time += proc_time
                result.append(idx)
            else:
                time = tasks[i][0]
        

        return result