# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            def bfs(left, right, level):
                if not left and not right:
                    return None
                if level % 2 != 0:
                    left.val, right.val = right.val, left.val
                bfs(left.left, right.right, level+1)
                bfs(left.right, right.left, level+1)
            bfs(root.left, root.right, 1)
        return root

            
        
                        


