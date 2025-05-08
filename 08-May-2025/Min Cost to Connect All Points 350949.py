# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        size = [0] * (n)
        def find(x):
            while x != parent[x] :
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x 
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 == r2:
                return False
            if size[r1] < size[r2]:
                parent[r1] = parent[r2]
                size[r2]+=size[r1]
            else:
                parent[r2] = parent[r1]
                size[r1]+=size[r2]
            return True
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j)) 
        edges.sort()
        ans = 0
        count = 0
        for cost, u, v in edges:
            if union(u, v):
                ans += cost
    
        return ans

        