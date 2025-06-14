# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        cur = 0
        ans = 0
        for r in range(len(nums)):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l +=1
            ans = max(ans, r-l +1)
            cur = cur | nums[r]
        return ans


        