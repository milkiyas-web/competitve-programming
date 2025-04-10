# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        p = defaultdict(list)
        color = [-1] * (n+1)
        for a, b in dislikes:
            p[a].append(b)
            p[b].append(a)
        def dfs(node, c):
            color[node] = c
            for ne in p[node]:
                if color[ne] == -1:
                    if not dfs(ne, 1-c):
                        return False
                elif color[ne] == c:
                    return False
            return True
        for i in range(1, n+1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
        