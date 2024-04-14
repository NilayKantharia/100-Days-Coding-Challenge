# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val
        self.helper(root.left)
        self.helper(root.right)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.helper(root)
        return self.sum

        
        
