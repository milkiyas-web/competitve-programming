# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        graph = defaultdict(list)
        ind = [0] * n
        for u,v in edges:
            ans[v].add(u)
            graph[u].append(v)
            ind[v] +=1
        de = deque()
        print(ans)
        print(graph)
        for i in range(len(ind)):
            if ind[i] == 0:
                de.append(i)
        while de:
            n = de.popleft()
            for ne in graph[n]:
                ans[ne].update(ans[n])
                ind[ne] -=1
                if ind[ne] == 0:
                    de.append(ne)
        return [sorted(val) for val in ans]




        
    