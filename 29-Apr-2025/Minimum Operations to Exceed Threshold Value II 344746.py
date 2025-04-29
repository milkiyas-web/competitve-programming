# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hp = nums
        heapq.heapify(hp)
        count = 0
        # 
        print(hp)
        while len(hp) > 0:
            x = heapq.heappop(hp)
            if x < k:
                count+=1
                y = heapq.heappop(hp)
                heapq.heappush(hp, x* 2 + y)
            # print(hp)
            else:
                break
            # if not check(hp):
            #     count+=1
        return count
        
            
                


        