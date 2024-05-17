class Solution:
    def dfs(self, root, target):
        if not root:
            return
        if self.dfs(root.left, target):
            root.left = None
        if self.dfs(root.right, target):
            root.right = None
        if not root.right and not root.left and root.val == target:
            return True
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return None if self.dfs(root, target) else root
