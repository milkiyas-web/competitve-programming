# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            cp = nums[i] - 1
            if cp >= len(nums):
                i += 1
                continue
            if nums[i] != nums[cp]:
                nums[i], nums[cp] = nums[cp], nums[i]
            else:
                i +=1
        print(nums)
        ans = []
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(i+1)
        return ans
        

        