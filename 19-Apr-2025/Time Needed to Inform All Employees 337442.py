# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(manager)):
            adj_list[manager[i]].append(i)
        de = deque([(headID, 0)])
        max_time = 0
        while de:
            i, time = de.popleft()
            max_time = max(max_time, time)
            for sub in adj_list[i]:
                de.append((sub, time+informTime[i]))
        return max_time
