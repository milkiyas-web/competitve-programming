# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ind = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            ind[b]+=1
        de = deque([])
        pre = defaultdict(set)
        for i in range(len(ind)):
            if ind[i] == 0:
                de.append(i)
        while de:
            n = de.popleft()
            # ind[n] -= 1

            for ne in graph[n]:
                pre[ne].add(n)
                for nodepre in pre[n]:
                    pre[ne].add(nodepre)
                ind[ne]-=1
                if ind[ne] == 0:
                    de.append(ne)
        ans = []
        for a, b in queries:
            if a in pre[b]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        print(graph)
        print(ind)