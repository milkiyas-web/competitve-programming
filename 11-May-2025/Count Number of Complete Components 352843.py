# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(v, ress):
            if v in visited:
                return
            visited.add(v)
            ress.append(v)
            for ne in adj[v]:
                dfs(ne, ress)
            return ress
        for i in range(n):
            if i in visited:
                continue
            component = dfs(i, [])
            if all([len(component) -1 == len(adj[j]) for j in component]):
                res+=1
            
        return res