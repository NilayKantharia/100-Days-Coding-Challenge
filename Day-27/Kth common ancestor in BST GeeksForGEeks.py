'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    
    def lca(self, root, x, y):
        if not root:
            return
        if root.data < x and root.data < y: return self.lca(root.right, x, y)
        elif root.data > x and root.data > y: return self.lca(root.left, x, y)
        else : return root
        
    def pathToLCA(self, root, lca):
        self.path.append(root.data)
        if root.data == lca.data : return
        elif root.data > lca.data : return self.pathToLCA(root.left, lca)
        else : return self.pathToLCA(root.right, lca)
        
    
    def kthCommonAncestor(self, root, k, x, y):
        lca = self.lca(root, x, y)
        self.path = []
        self.pathToLCA(root,lca)
            
        if len(self.path) < k: return -1
        n = len(self.path)
        return self.path[n - k]
