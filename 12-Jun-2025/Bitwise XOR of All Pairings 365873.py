# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 =  len(nums2)
        x = 0
        if n1 % 2 == 1:
            for val in nums2:
                x ^= val
        if n2 % 2 == 1:
            for val in nums1:
                x ^= val
        return x






        