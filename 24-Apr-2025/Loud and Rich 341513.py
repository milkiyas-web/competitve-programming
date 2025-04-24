# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        # ind = [-1] * n
        ans = [-1] * n
        for a, b in richer:
            graph[b].append(a)
        def dfs(i):
            if ans[i] != -1:
                return
            ans[i] = i
            for ne in graph[i]:
                dfs(ne)
                if quiet[ans[ne]] < quiet[ans[i]]:
                    ans[i] = ans[ne]
                
        for i in range(n):
            if ans[i] == -1:
                dfs(i)
        return ans