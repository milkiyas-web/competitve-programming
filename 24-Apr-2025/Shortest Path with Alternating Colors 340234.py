# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for s, d in redEdges:
            red[s].append(d)
        for s, d in blueEdges:
            blue[s].append(d)
        
        ans = [-1] * n
        queue = deque()
        queue.append((0, 0, None)) 
        visited = set()
        visited.add((0, None))

        while queue:
            node, dist, prev_color = queue.popleft()
            if ans[node] == -1:
                ans[node] = dist
            
            if prev_color != "RED":
                for neighbor in red[node]:
                    if (neighbor, "RED") not in visited:
                        visited.add((neighbor, "RED"))
                        queue.append((neighbor, dist + 1, "RED"))

            if prev_color != "BLUE":
                for neighbor in blue[node]:
                    if (neighbor, "BLUE") not in visited:
                        visited.add((neighbor, "BLUE"))
                        queue.append((neighbor, dist + 1, "BLUE"))

        return ans
