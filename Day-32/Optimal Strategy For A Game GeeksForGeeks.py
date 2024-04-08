class Solution:
    def solve(self, arr, l, r):
        if l > r: return 0
        if l == r: return arr[l]
        if self.dp[l][r] != -1: return self.dp[l][r]
        
        left = arr[l] + min(self.solve(arr, l + 2, r), self.solve(arr, l + 1, r - 1))
        right = arr[r] + min(self.solve(arr, l, r - 2), self.solve(arr, l + 1, r - 1))
        self.dp[l][r] = max(left, right)
        return self.dp[l][r]
        
    def optimalStrategyOfGame(self,n, arr):
        self.dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        self.solve(arr, 0, n-1)
        return self.dp[0][n-1]
