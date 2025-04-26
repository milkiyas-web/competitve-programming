# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        ind = [0] * numCourses
        de = deque([])
        for a,b in prerequisites:
            graph[a].append(b)
            ind[b] +=1
        for i in range(numCourses):
            if ind[i] == 0:
                de.append(i)
        ans = []

        while de:
            n = de.popleft()
            ans.append(n)
            for ne in graph[n]:
                ind[ne] -= 1
                if ind[ne] == 0:
                    de.append(ne)
        print(ans)
        if len(ans) == numCourses:
            return True
        else:
            return False
            
