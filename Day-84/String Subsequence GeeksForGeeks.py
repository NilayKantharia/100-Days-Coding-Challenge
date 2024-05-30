class Solution:
    def subSequence(self, s1, s2, i, j, dp, mod):
        if j < 0:
            return 1
        if i < 0:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = (self.subSequence(s1, s2, i-1, j-1, dp, mod) % mod + self.subSequence(s1, s2, i-1, j, dp, mod) % mod) % mod
        else:
            dp[i][j] = self.subSequence(s1, s2, i-1, j, dp, mod) % mod
        return dp[i][j]
        
    def countWays(self, s1 : str, s2 : str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        mod = 10**9 + 7
        if(n2 > n1):
            return 0
        dp = [[-1 for i in range(n2 + 1)] for j in range(n1 + 1)]
        return self.subSequence(s1, s2, n1-1, n2-1, dp, mod)
