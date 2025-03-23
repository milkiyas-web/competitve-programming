# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    perm(path)
                    path.pop()
        perm([])
        return res
            
        