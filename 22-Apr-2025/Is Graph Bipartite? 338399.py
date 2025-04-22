# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visit = [0] * n
        def bfs(i):
            if visit[i] != 0:
                return True
            de = deque([i])
            visit[i] = -1
            while de:
                node = de.popleft()
                for ne in graph[node]:
                    if visit[ne] != 0 and visit[ne] == visit[node]:
                        return False
                    elif visit[ne] == 0:
                        de.append(ne)
                        visit[ne] = -1 * visit[node]
            return True


        for i in range(n):
           if not bfs(i):
            return False
        return True
