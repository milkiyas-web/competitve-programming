# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1<<n): #2**m
            dummy = list()
            for j in range(n):
                if (1<<j) & i:
                    dummy.append(nums[j])
            ans.append(dummy)
        return ans



        