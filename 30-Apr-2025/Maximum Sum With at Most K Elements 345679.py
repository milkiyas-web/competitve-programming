# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        hp = []
        for i in range(n):
            grid[i].sort(reverse=True)
        for i in range(n):
            for j in range(limits[i]):
                heapq.heappush(hp, grid[i][j])
    
        while len(hp) > k:
            heapq.heappop(hp)
            # print(hp)
        
        return sum(hp)



        