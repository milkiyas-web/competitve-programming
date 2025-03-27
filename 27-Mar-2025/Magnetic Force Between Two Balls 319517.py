# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, max(position)
        def is_valid(mid):
            count, prev_idx = 1, 0
            for i in range(len(position)):
                if position[i] - position[prev_idx] >= mid:
                    prev_idx = i
                    count+=1
            return count >= m
                    
        ans = 0
        
        while l <= r:
            mid = (l+r) // 2
            if is_valid(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans

