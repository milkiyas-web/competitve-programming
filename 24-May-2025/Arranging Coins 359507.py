# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        coin=0
        num=n
        for i in range(1,n+1):
            if num-i>=0:
                coin+=1
                num=num-i
            else:
                break
        return coin
        