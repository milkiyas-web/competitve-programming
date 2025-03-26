# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        

        if sum(nums) == 0:
            return 0

        l, r = 1, len(queries)
        n = len(nums)

        def is_valid(m):
            pr_sum = [0] * (n+1)
            for i in range(m):
                left, right, val = queries[i]
                pr_sum[left] +=val
                pr_sum[right+1] -=val
            curr = 0
            for i in range(n):
                curr+=pr_sum[i]
                if curr<nums[i]:
                    return False
            return True
        # if not is_valid(m):
        #     return -1
        res = r
        if not is_valid(r):
            return -1
        while l < r:
            mid = (l+r)//2
            if is_valid(mid):
                res = min(res, mid)
                r = mid
            else:
                l = mid+1
        return l