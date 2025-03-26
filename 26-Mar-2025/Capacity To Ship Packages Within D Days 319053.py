# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(m):
            ships, cur_c = 1, m
            for w in weights:
                if cur_c -w  < 0:
                    ships +=1
                    cur_c=m
                cur_c -=w
            return ships<=days
        
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (l+r) // 2
            if can_ship(mid):
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1
        return l


        
        