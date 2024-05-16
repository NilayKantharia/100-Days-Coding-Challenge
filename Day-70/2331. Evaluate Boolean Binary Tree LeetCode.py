class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return root.val
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        return left or right if root.val == 2 else left and right
