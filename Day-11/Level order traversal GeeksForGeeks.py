class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        res=[]
        if not root:
            return
        queue=[]
        queue.append(root)
        while len(queue)>0:
            res.append(queue[0].data)
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
        
