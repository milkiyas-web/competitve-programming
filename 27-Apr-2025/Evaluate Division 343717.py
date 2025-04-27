# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
       
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        # def dfs(a, b, visited):
        #     visited.add(a)
        #     if a == b:
        #         return 1
        #     for ne, value in graph[a]:
                
        #         if ne in visited:
        #             continue
        #         print(ne)
        #         visited.add(ne)
        #         prev = value
        #         if (a, b) == (ne, a):
        #             return value
        #         else:
        #             return value*value
        #         # else:
        #         #     return value*value
        #         dfs(a, ne, visited)
        #         # if res > 0:
        #         #     return ne * value
        #         # print(res)
        # for a, c in queries:
        #     if c not in graph and a not in graph:
        #         ans.append(-1.0)
        #     else:
        #         ans.append(dfs(a,c, set()))
        # print(graph)
        # return ans
        def bfs(src, tar):
            if src not in adj or tar not in adj:
                return -1
            de = deque()
            visited = set()
            de.append([src, 1])
            visited.add(src)
            while de:
                n, w = de.popleft()
                if n == tar:
                    return w
                for ne, we in adj[n]:
                    if ne not in visited:
                        de.append([ne, we*w])
                        visited.add(ne)
            return -1



        return [bfs(que[0], que[1]) for que in queries]
            


        
