# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        ans = 0
        for i in range(len(heights)-1):
            d = heights[i+1] - heights[i]
            if d > 0:
                heappush(hp, d)
                if len(hp) > ladders:
                    bricks-=heappop(hp)
                if bricks < 0:
                    return i
        return len(heights)-1