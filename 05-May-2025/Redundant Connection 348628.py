# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            x_ = find(x)
            y_ = find(y)
            if x_ == y_:
                return False
            if rank[x_] > rank[y_]:
                parent[y_] = x_
                rank[x_] += rank[y_]
            else:
                parent[x_] = y_
                rank[y_]+=rank[x_]
            return True


        for a,b in edges:
            if not union(a,b):
                return [a,b]



            