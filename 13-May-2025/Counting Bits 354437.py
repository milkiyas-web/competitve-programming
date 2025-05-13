# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def rec(n):
            if n==1:
                return 1
            if n==0:
                return 0
            return rec(n//2) + n%2
        for i in range(n+1):
            ans.append(rec(i))
            
        return ans
       
        

        