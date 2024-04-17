# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, current):
        if not root:
            return
        current = chr(ord('a') + root.val) + current
        if root.left and root.right:
            return min(self.dfs(root.left, current), self.dfs(root.right, current))
        
        if root.left:
            return self.dfs(root.left, current)
        if root.right:
            return self.dfs(root.right, current)
        
        return current

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        current = ''
        return self.dfs(root, current)
