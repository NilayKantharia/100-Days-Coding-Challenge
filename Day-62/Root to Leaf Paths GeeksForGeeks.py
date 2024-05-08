class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        res = []
        def dfs(root, curr):
            if not root:
                return 
            if not root.right and not root.left:
                res.append(curr + [root.data])
                return
            dfs(root.left, curr + [root.data])
            dfs(root.right, curr + [root.data])
        dfs(root, [])
        return res
        

