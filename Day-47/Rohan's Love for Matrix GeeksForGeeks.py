class Solution:
    def firstElement (self, n):
        if n == 1 or n == 0:
            return 1
        mod = 1000000007
        a = 1
        b = 1
        for i in range(n - 2):
            c = (a + b) % mod
            a = b
            b = c
        return c % mod
