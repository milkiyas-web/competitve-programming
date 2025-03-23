# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def com(num, temp):
            if temp and len(temp) == k:
                ans.append(temp.copy())
                return
            for i in range(num, n+1):
                temp.append(i)
                com(i+1, temp)
                temp.pop()

        com(1, [])
        return ans
            

        