# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            cp = nums[i] - 1
            if nums[i] != nums[cp]:
                nums[i], nums[cp] = nums[cp], nums[i]
            else:
                i+=1
        print(nums)
        ans = []
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])
                ans.append(i+1)
                
    
        return ans
        
