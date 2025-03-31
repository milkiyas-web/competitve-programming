# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        # def is_valid(mid):
        ans = False    
        while l<=r:
            mid = (l+r)//2
            # if target in matrix[mid]:
            if target > matrix[mid][-1]:
                # ans = True
                l = mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                break
        if l > r:
            return False
        row = matrix[(l + r) // 2]
        left, right = 0, len(row)-1
        while left <= right:
            mid = (left+right) // 2
            if row[mid] == target:
                return True
            if target > row[mid]:
                left = mid+1
            elif target < row[mid]:
                right = mid-1
        
        return False
        
        