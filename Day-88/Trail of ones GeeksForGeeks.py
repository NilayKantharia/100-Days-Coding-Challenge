class Solution:
    def numberOfConsecutiveOnes (ob,n):
        a = [0] * n
        b = [0] * n
        mod = 10**9 + 7
        a[0], b[0] = 1, 1
        for i in range(1, n):
            a[i] = a[i-1]+b[i-1] % mod
            b[i] = a[i-1]
        return ((1 << n)%mod - a[n - 1] - b[n - 1])%mod
