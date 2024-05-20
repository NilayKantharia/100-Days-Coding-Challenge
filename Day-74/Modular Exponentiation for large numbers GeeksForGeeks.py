class Solution:
	def PowMod(self, x, n, m):
	    res = 1
        x = x % m
        while n:
            if (n % 2) == 1:
                res = (res * x) % m
            n = n // 2
            x = (x * x) % m
        return res
