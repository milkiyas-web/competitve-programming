# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def max_diff(root, max_num, min_num):
            if not root:
                return max_num - min_num
            max_num = max(max_num, root.val)
            min_num = min(min_num, root.val)

            left_max = max_diff(root.left, max_num, min_num)
            right_max = max_diff(root.right, max_num, min_num)

            return max(left_max, right_max)
        return max_diff(root, root.val, root.val)
            
        
        

        

        