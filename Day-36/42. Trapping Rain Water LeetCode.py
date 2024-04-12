class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]
        for i in range(1,n):
            leftMax[i] = max(height[i], leftMax[i - 1])
        
        for i in range(n-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        
        trappedWater = 0
        for i in range(n):
            trappedWater += min(leftMax[i], rightMax[i]) - height[i]
        
        return trappedWater
