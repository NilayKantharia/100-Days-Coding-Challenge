# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,curr):
        if not root:
            return

        curr += root.val

        if not root.right and not root.left:
            self.sum += curr
            
        self.dfs(root.left, curr*10)
        self.dfs(root.right, curr*10)
        return

        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
        
