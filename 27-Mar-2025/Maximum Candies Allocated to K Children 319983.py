# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)

        if sum(candies) < k:
            return 0
        def is_valid(mid):
            res = 0
            for c in candies:
                res+=c//mid
            return res>=k
        ans = 0 
        while l <= r:
            mid = (l+r)//2
            if is_valid(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans
