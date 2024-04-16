# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val, depth, currDepth):
        if not root:
            return
        if currDepth < depth - 1:
            self.helper(root.left, val, depth, currDepth + 1)
            self.helper(root.right, val, depth, currDepth + 1)
        
        if currDepth == depth - 1:
            tempLeft = root.left
            tempRight = root.right
            newLeft = TreeNode(val)
            newRight = TreeNode(val)
            root.left = newLeft
            root.right = newRight
            newLeft.left = tempLeft
            newRight.right = tempRight


    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        
        self.helper(root, val, depth, 1)
        return root
