class Solution:
    def series(self, n):
        ans = [0]*(n+1)
        ans[0] = 0
        ans[1] = 1
        mod=(10**9) + 7
        
        for i in range(2,n+1):
            ans[i] = (ans[i-1] + ans[i-2]) % mod
        return ans

