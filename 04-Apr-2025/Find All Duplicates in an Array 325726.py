# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dubs_set = set()
        result = []
        for num in nums:
            if num in dubs_set:
                result.append(num)
            else:
                dubs_set.add(num)
        return result
            


        