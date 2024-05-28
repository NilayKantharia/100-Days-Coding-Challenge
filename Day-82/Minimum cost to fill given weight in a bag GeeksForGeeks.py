class Solution:
    def takeNotTake(self, i, w, dp, cost):
        if w == 0:
            return 0
        if i >= len(cost) or i + 1 > w:
            return 1000000
        if dp[i][w] != -1: return dp[i][w]
        a=0
        b=0
        if cost[i] != -1 and i+1 <= w:
            a=cost[i]+self.takeNotTake(i, w-(i+1), dp, cost)
        b=self.takeNotTake(i+1, w, dp, cost)
        dp[i][w]=min(a, b)
        return dp[i][w]
            
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        dp=[[-1 for i in range(w+2)] for j in range(n+2)]
        res = self.takeNotTake(0, w, dp, cost)
        return -1 if res >= 1000000 else res
