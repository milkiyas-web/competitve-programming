# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ## using a max heap to find the smallest k num.
        n = len(matrix)
        hp = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(hp, -matrix[i][j])
        heapq.heapify(hp)
        while len(hp) > k:
            heapq.heappop(hp)
        print(hp)
        return -hp[0]
        