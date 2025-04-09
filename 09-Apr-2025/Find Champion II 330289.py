# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champ=[0]*n
        for a, b in edges:
            champ[b]+=1
        res = []
        for i in range(n):
            if champ[i] == 0:
                res.append(i)
        if len(res) > 1:
            return -1
        else:
            return res[0]

        