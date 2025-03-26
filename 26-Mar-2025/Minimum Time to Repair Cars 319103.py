# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, max(ranks) * (cars**2)
        def is_valid(m):
            k = 0
            for r in ranks:
                k+=floor(sqrt(m//r))
            return k>= cars
        while l < r:
            mid = (l+r)//2
            if is_valid(mid):
                r=mid
            else:
                l= mid+1
        return l



