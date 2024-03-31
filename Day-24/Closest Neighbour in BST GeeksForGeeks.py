class Solution:
    
    def traverse(self, root, n):
        if not root:
            return
        if root.key <= n:
            self.res = max(self.res, root.key)
        self.traverse(root.left, n)
        self.traverse(root.right, n)
        
    def findMaxForN(self, root, n):
        self.res = 0
        self.traverse(root, n)
        return self.res if self.res else -1

