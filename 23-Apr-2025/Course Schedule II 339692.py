# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        ind = [0] * numCourses
        for a,b in pre:
            adj[b].append(a)
            ind[a] += 1
        
        de = deque()
        # for i, d in enumerate(ind):
        #     if d == 0:
        #         de.append(i)
        for i in range(len(ind)):
            if ind[i] == 0:
                de.append(i)
       
        ans = []
        while de:
            n = de.popleft()
            ans.append(n)
            for c in adj[n]:
            
                ind[c] -= 1
                
                if ind[c] == 0:
                    de.append(c)
        if len(ans) != numCourses:
            return []
        return ans
