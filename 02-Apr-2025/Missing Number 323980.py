# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)

        while l < r:
            mid = (l+r) // 2
            if nums[mid] == mid:
                l = mid+1
            else:
                r = mid
        return l
        