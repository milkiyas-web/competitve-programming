# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        
        de = deque()
        de.append(k - 1)
        res = [math.inf for _ in range(n)]
        res[k-1] = 0

        while de:
            for _ in range(len(de)):
                node = de.popleft()
                for ne, val in graph[node]:
                    if val + res[node] < res[ne]:
                        res[ne] = val + res[node]
                        de.append(ne)
        ans = max(res)
        if ans == math.inf:
            return -1
        else:
            return ans



        