class Solution:
    def helper(self, root, sumOfHeight, currentHeight):
        if not root:
            return
        if not root.left and not root.right:
            sumOfHeight += root.data
            if currentHeight > self.height:
                self.res = sumOfHeight
                self.height = currentHeight
            elif currentHeight == self.height:
                self.res = max(sumOfHeight,self.res)
            return
        sumOfHeight += root.data
        self.helper(root.left, sumOfHeight, currentHeight+1)
        self.helper(root.right, sumOfHeight, currentHeight+1)
            
    def sumOfLongRootToLeafPath(self,root):
        sumOfHeight = 0
        currentHeight = 0
        self.height = 0
        self.res = 0
        self.helper(root, sumOfHeight, currentHeight)
        return self.res

