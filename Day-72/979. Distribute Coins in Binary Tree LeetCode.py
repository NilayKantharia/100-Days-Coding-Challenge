class Solution:
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        extra = root.val + left + right - 1
        self.res += abs(extra)
        return extra
        
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
