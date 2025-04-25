# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = defaultdict(list)
        out = [0] * n
        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
            out[i] = len(graph[i])
        print(adj)
        print(out)
        de = deque([])
        ans = []
        for i in range(len(out)):
            if out[i] == 0:
                de.append(i)
        while de:
            node = de.popleft()
            ans.append(node)
            for ne in adj[node]:
                out[ne] -=1
                if out[ne] == 0:
                    de.append(ne)
            
        ans.sort()
        print(de)
        return ans