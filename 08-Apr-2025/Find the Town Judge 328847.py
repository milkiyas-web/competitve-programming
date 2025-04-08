# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ind = defaultdict(int)
        od = defaultdict(int)

        for a, b in trust:
            od[a] +=1 
            ind[b] +=1
        for i in range(1, n+1):
            if od[i] == 0 and ind[i] == n-1:
                return i
        return -1
        

            

        